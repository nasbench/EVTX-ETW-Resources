"""Helpers shared by etw-to-csv.py and stats.py."""
import re
import sys
import xml.etree.ElementTree as ET

# Returned by parse_etw_xml() for manifests that have no event metadata
EMPTY_PROVIDER = "Empty Provider"

# Manifests that could not be read. The scripts report them and exit non-zero.
ERRORS = []

_ARGUMENT = re.compile(r"%(\d+)")
_UNSAFE_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|]')
_LINE_BREAKS = re.compile(r"\s*\n\s*")

# Event element -> key of the dict returned for every event
_EVENT_FIELDS = (
    ("Id", "eid"),
    ("Version", "version"),
    ("Channel", "channel"),
    ("Level", "level"),
    ("Task", "task"),
    ("Opcode", "opcode"),
    ("Keyword", "keyword"),
    ("Message", "message"),
    ("Template", "template"),
)


def one_line(text):
    """Turn line breaks (and the blanks around them) into single spaces.

    The CSVs hold one event per line, and removing the breaks outright glued
    sentences together ("...was changed.Subject:").
    """
    return _LINE_BREAKS.sub(" ", text or "").strip()


def safe_filename(name):
    """Make a provider name usable as a file name ("TCP/IP" -> "TCP_IP")."""
    return _UNSAFE_FILENAME_CHARS.sub("_", name)


def template_fields(template):
    """Names of the data items of an event template, in argument order."""
    try:
        root = ET.fromstring(template.strip())
    except ET.ParseError:
        return []
    return [item.get("name", "") for item in root]


def fixMessage(message, template):
    """Replace the "%N" arguments of a message with the template field names.

    The message of an ETW event looks like "Process %1 started at time %2",
    where %N is the Nth data item of the template. All arguments are replaced
    in one pass: replacing %1 first would also clobber the start of %10-%19.
    Arguments without a matching field are left untouched.
    """
    fields = template_fields(template)

    def replace(match):
        index = int(match.group(1))
        if 1 <= index <= len(fields) and fields[index - 1]:
            return "{" + fields[index - 1] + "}"
        return match.group(0)

    return _ARGUMENT.sub(replace, message)


def _error(message):
    ERRORS.append(message)
    print(message, file=sys.stderr)


def parse_etw_xml(file_path):
    """Parse one provider manifest.

    Returns {"provider_name": str, "events": [dict, ...]}, or EMPTY_PROVIDER
    when the manifest holds no event metadata or cannot be read (the latter
    is recorded in ERRORS).
    """
    try:
        root = ET.parse(file_path).getroot()
    except (ET.ParseError, OSError) as error:
        _error(f"Cannot read {file_path}: {error}")
        return EMPTY_PROVIDER

    provider = root.find("Provider")
    if provider is None or provider.find("EventMetadata") is None:
        print(f"No event metadata, skipping: {file_path}")
        return EMPTY_PROVIDER

    events = []
    for event in provider.find("EventMetadata").findall("Event"):
        parsed = {key: one_line(event.findtext(tag)) for tag, key in _EVENT_FIELDS}
        events.append(parsed)

    return {"provider_name": provider.findtext("Name", ""), "events": events}


def md_table(table, padding=2):
    """Render rows (the first one is the header) as a Markdown table.

    Cells are padded to the width of their column, like the csvtomd package
    this replaces.
    """
    columns = max(len(row) for row in table)
    rows = [list(row) + [""] * (columns - len(row)) for row in table]
    widths = [max(len(row[i]) for row in rows) for i in range(columns)]
    pad = " " * padding

    def line(cells):
        return (pad + "|" + pad).join(cell.ljust(width) for cell, width in zip(cells, widths)).rstrip()

    divider = ("-" * padding + "|" + "-" * padding).join("-" * width for width in widths)
    return "\n".join([line(rows[0]), divider] + [line(row) for row in rows[1:]])


def parse_build_folder(name):
    """Split a build folder name into its parts.

    "WindowsServer2025_24H2_Standard_20260113_26100.32230" gives the
    Windows name ("Windows Server 2025"), version ("24H2"), edition
    ("Standard"), date ("2026/01/13") and build ("26100.32230").
    """
    parts = name.split("_")
    head = parts[0]
    if head.startswith("WindowsServer"):
        windows = "Windows Server " + head[len("WindowsServer"):]
    else:
        windows = "Windows " + head[1:]
    date = ""
    if len(parts) > 3:
        date = parts[3][0:4] + "/" + parts[3][4:6] + "/" + parts[3][6:8]
    return {
        "windows": windows,
        "version": parts[1],
        "edition": parts[2],
        "date": date,
        "build": parts[4] if len(parts) > 4 else "",
    }


def _number(text):
    try:
        return int(text)
    except ValueError:
        return 0


def build_sort_key(build):
    """Sort key of a "26100.32230" build: compare the parts as numbers.

    Parsing the build as a float ("26100.2" > "26100.1742") sorts the update
    revision wrongly.
    """
    return tuple(_number(part) for part in build.split("."))
