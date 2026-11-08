import pytest

from etwlib import fixMessage, parse_etw_xml

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


@pytest.mark.xfail(strict=True, reason="%1 is replaced inside %10..%19 (fixed in a follow-up)")
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
    assert parse_etw_xml(str(path)) == "Empty Provider"
