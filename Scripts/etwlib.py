"""Helpers shared by etw-to-csv.py and stats.py."""
import re
import sys
import xml.etree.ElementTree as ET

# Returned by parse_etw_xml() for manifests that have no event metadata
EMPTY_PROVIDER = "Empty Provider"

# Manifests that could not be read. The scripts report them and exit non-zero.
ERRORS = []

_ARGUMENT = re.compile(r"%([1-9]\d*)")
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
