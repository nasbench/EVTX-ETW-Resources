import pytest

import etwlib
from etwlib import EMPTY_PROVIDER, fixMessage, one_line, parse_etw_xml, safe_filename

TEMPLATE = (
    '<template xmlns="http://schemas.microsoft.com/win/2004/08/events">'
    '<data name="ProcessID" inType="win:UInt32"/>'
    '<data name="CreateTime" inType="win:FILETIME"/>'
    '<data name="ImageName" inType="win:UnicodeString"/>'
    "</template>"
)

MANIFEST = """<Providers>
    <Provider>
        <Name>Test-Provider</Name>
        <Metadata><Guid>{00000000-0000-0000-0000-000000000001}</Guid></Metadata>
        <EventMetadata>
            <Event>
                <Id>1</Id>
                <Version>0</Version>
                <Channel>Test/Operational</Channel>
                <Level>Information</Level>
                <Task>ProcessStart</Task>
                <Opcode>Start</Opcode>
                <Keyword>TEST_KEYWORD</Keyword>
                <Message><![CDATA[
Process %1 started at %2 with name %3.]]></Message>
                <Template><![CDATA[
@@TEMPLATE@@
]]></Template>
            </Event>
        </EventMetadata>
    </Provider>
</Providers>
""".replace("@@TEMPLATE@@", TEMPLATE)


def test_fix_message_replaces_arguments():
    assert (
        fixMessage("Process %1 started at %2 with name %3.", TEMPLATE)
        == "Process {ProcessID} started at {CreateTime} with name {ImageName}."
    )


def test_fix_message_without_template_is_unchanged():
    assert fixMessage("Process %1 started.", "") == "Process %1 started."


def test_fix_message_two_digit_arguments():
    names = "".join('<data name="F%d"/>' % i for i in range(1, 13))
    template = '<template xmlns="x">%s</template>' % names
    assert fixMessage("%10 and %12", template) == "{F10} and {F12}"


def test_parse_etw_xml(tmp_path):
    path = tmp_path / "Test-Provider.xml"
    path.write_text(MANIFEST, encoding="utf-8")
    parsed = parse_etw_xml(str(path))
    assert parsed["provider_name"] == "Test-Provider"
    (event,) = parsed["events"]
    assert event["eid"] == "1"
    assert event["version"] == "0"
    assert event["channel"] == "Test/Operational"
    assert event["level"] == "Information"
    assert event["task"] == "ProcessStart"
    assert event["opcode"] == "Start"
    assert event["keyword"] == "TEST_KEYWORD"
    assert event["message"] == "Process %1 started at %2 with name %3."


def test_parse_etw_xml_skips_manifest_without_event_metadata(tmp_path):
    path = tmp_path / "Empty.xml"
    path.write_text(
        "<Providers><Provider><Name>Empty</Name><Metadata/></Provider></Providers>",
        encoding="utf-8",
    )
    assert parse_etw_xml(str(path)) == EMPTY_PROVIDER


def test_fix_message_leaves_unknown_arguments():
    assert fixMessage("%1 %5", '<template xmlns="x"><data name="A"/></template>') == "{A} %5"


def test_one_line_keeps_sentences_apart():
    assert one_line("\nThe system time was changed.\n\nSubject:\n\tSecurity ID:\t%1\n") == "The system time was changed. Subject: Security ID:\t%1"


def test_safe_filename():
    assert safe_filename("TCP/IP") == "TCP_IP"
    assert safe_filename("Microsoft-Windows-Kernel-Process") == "Microsoft-Windows-Kernel-Process"


def test_parse_etw_xml_keeps_commas_and_quotes(tmp_path):
    path = tmp_path / "P.xml"
    path.write_text(MANIFEST.replace("Process %1 started", 'Process "%1", started'), encoding="utf-8")
    (event,) = parse_etw_xml(str(path))["events"]
    assert event["message"].startswith('Process "%1", started')


def test_parse_etw_xml_reports_malformed_manifest(tmp_path):
    path = tmp_path / "Broken.xml"
    path.write_text("<Providers><Provider>", encoding="utf-8")
    etwlib.ERRORS.clear()
    assert parse_etw_xml(str(path)) == EMPTY_PROVIDER
    assert len(etwlib.ERRORS) == 1
    etwlib.ERRORS.clear()


def test_md_table_matches_csvtomd():
    # Expected text generated with csvtomd.md_table(table, padding=2)
    table = [["ETW Provider", "Number Of Events"], ["Microsoft-Windows-Kernel-Process", "73"], ["A", "5"], ["Jagged"]]
    assert etwlib.md_table(table, padding=2) == 'ETW Provider                      |  Number Of Events\n----------------------------------|------------------\nMicrosoft-Windows-Kernel-Process  |  73\nA                                 |  5\nJagged                            |'


def test_parse_build_folder():
    assert etwlib.parse_build_folder("WindowsServer2025_24H2_Standard_20260113_26100.32230") == {
        "windows": "Windows Server 2025",
        "version": "24H2",
        "edition": "Standard",
        "date": "2026/01/13",
        "build": "26100.32230",
    }
    assert etwlib.parse_build_folder("W11_22H2_Pro_20221018_22621.674")["windows"] == "Windows 11"


def test_build_sort_key_compares_numbers():
    builds = ["26100.2", "26100.1742", "26100.32230", "19045"]
    assert sorted(builds, key=etwlib.build_sort_key, reverse=True) == ["26100.32230", "26100.1742", "26100.2", "19045"]
    # as floats 26100.2 would sort above 26100.1742
    assert float("26100.2") > float("26100.1742")


def test_provider_csv_lists_the_newest_build_first(tmp_path, monkeypatch):
    import stats

    builds = ["W10_1507_Pro_20150729_10240", "W10_1507_Pro_20150805_10240.1", "W10_1507_Pro_20150901_10240.20", "W10_1507_Pro_20150902_10240.9"]
    for build in builds:
        folder = tmp_path / "ETWProvidersManifests" / "Windows10" / "1507" / build / "WEPExplorer"
        folder.mkdir(parents=True)
        (folder / "Test-Provider.xml").write_text(MANIFEST, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    providers = stats.getProvidersPaths([str(p.parent) for p in (tmp_path / "ETWProvidersManifests").glob("*/*/*/WEPExplorer/Test-Provider.xml")])
    stats.createProvidersCSV(providers, "Internal")

    import csv

    with open(tmp_path / "ETWProvidersCSVs" / "Internal" / "Test-Provider.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # "10240" has no update revision: it is the oldest, not the newest
    assert [row["Build"] for row in rows] == ["10240.20", "10240.9", "10240.1", "10240"]
