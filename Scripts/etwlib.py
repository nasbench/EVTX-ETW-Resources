"""Helpers shared by etw-to-csv.py and stats.py."""
import xml.etree.ElementTree as ET

# This function replaces the variables inside the data with their corresponding values in the templates. For example:
# If we look at an ETW manifest the message section of an event looks like this : "Process %1 started at time %2 by parent %3 running in session %4 with name %5"
# This function replaces the "%" with their corresponding values
def fixMessage(message, template):
    try:
        parsedTemplate = ET.fromstring(template)
    except:
        parsedTemplate = []
    listOfTemplateAttributes = [""]
    for e in parsedTemplate:
        listOfTemplateAttributes.append(e.attrib['name'])
    
    for i in range(len(listOfTemplateAttributes)-1):
        message = message.replace("%"+str(i+1), "{" + listOfTemplateAttributes[i+1] + "}")
    
    return message

def parse_etw_xml(file_path):
    
    # This is used to skip "empty" ETW manifest
    skip = False
    root = ET.parse(file_path).getroot()
    try:
        if root[0][0].tag == "Name":
            provider_name = root[0][0].text
        else:
            provider_name = ""
    except IndexError:
        print(f"Name - IndexError while reading the file : {file_path}")

    try:
        if root[0][2].tag == "EventMetadata":
            eventMetaData = root[0][2]
        else:
            eventMetaData = ""
    except IndexError:
            print(f"EventMetaData - IndexError while reading the file : {file_path}")
            skip = True

    if not skip:
        events_list = []
        for event in eventMetaData:
            event_dict = {}
            event_dict['eid'] = event[0].text
            event_dict['channel'] = ""
            event_dict['message'] = ""
            event_dict['version'] = ""
            event_dict['level'] = ""
            event_dict['task'] = ""
            event_dict['opcode'] = ""
            event_dict['keyword'] = ""
            
            for data in event:
                if data.tag == "Channel":
                    event_dict['channel'] = data.text
                elif data.tag == "Message":
                    #Replacing the "," with ";" and removing double quotes just so the CSV behave nicely
                    event_dict['message'] = data.text.replace("\n","").replace(",", ";") .replace("\"", "'")
                elif data.tag == "Template":
                    event_dict['template'] = data.text.replace("\n", "").replace(",", ";")
                elif data.tag == "Version":
                    event_dict['version'] = data.text.replace("\n", "").replace(",", ";")
                elif data.tag == "Level":
                    event_dict['level'] = data.text.replace("\n", "").replace(",", ";")
                elif data.tag == "Task":
                    event_dict['task'] = data.text.replace("\n", "").replace(",", ";")
                elif data.tag == "Opcode":
                    event_dict['opcode'] = data.text.replace("\n", "").replace(",", ";")
                elif data.tag == "Keyword":
                    event_dict['keyword'] = data.text.replace("\n", "").replace(",", ";")


            events_list.append(event_dict)
        
        etw_provider_dict = {}
        etw_provider_dict["provider_name"] = provider_name
        etw_provider_dict["events"] = events_list

        return etw_provider_dict
    else:
        return "Empty Provider"
