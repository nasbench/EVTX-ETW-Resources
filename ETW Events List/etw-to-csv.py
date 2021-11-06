import xml.etree.ElementTree as ET
from optparse import OptionParser
import os
import csvtomd

def convertCsvToMD(fileName, folderName):

    with open("CSV/" + folderName + "/" + fileName + ".csv", "r") as f:
        table = csvtomd.csv_to_table(f, ",")
    
    if table:
        with open("Markdown/" + folderName + "/" + fileName + ".md", "w") as f:
            f.write(
                csvtomd.md_table(table, padding=2)
            )
    else:
        print("Cannot Convert to Markdown")


#From: https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        if entry != "All.xml":
            if os.path.splitext(entry)[1] == ".xml":
                # Create full path
                fullPath = os.path.join(dirName, entry)
                # If entry is a directory then get the list of files in this directory 
                if os.path.isdir(fullPath):
                    allFiles = allFiles + getListOfFiles(fullPath)
                else:
                    allFiles.append(fullPath)
                
    return allFiles

def parse_etw_xml(file_path):
    
    # This is used to skip "empty" ETW manifest
    skip = False
    root = ET.parse(file_path).getroot()

    if root[0][0].tag == "Name":
        provider_name = root[0][0].text
    else:
        provider_name = ""

    try:
        if root[0][2].tag == "EventMetadata":
            eventMetaData = root[0][2]
        else:
            eventMetaData = ""
    except IndexError:
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

# This function replaces the variables inside the data with their corresponding values in the templates. For example:
# If we look at an ETW manifest the message section of an event looks like this : "Process %1 started at time %2 by parent %3 running in session %4 with name %5"
# This function replaces the "%" with their corresponding values
def fixMessage(message, template):

    parsedTemplate = ET.fromstring(template)
    listOfTemplateAttributes = [""]
    for e in parsedTemplate:
        listOfTemplateAttributes.append(e.attrib['name'])
    
    for i in range(len(listOfTemplateAttributes)-1):
        message = message.replace("%"+str(i+1), "{" + listOfTemplateAttributes[i+1] + "}")
    
    return message

def converterStart(parsed_provider, folderName):
    header = "Provider,Level,Event ID,Version,Channel,Task,Opcode,Keyword,Message"
    with open("CSV/" + folderName + "/" + parsed_provider["provider_name"] + ".csv", "w") as f:
        f.write(header)
        f.write("\n")
        for i in parsed_provider["events"]:
            fixed_message = ""
            if i['template'] != "":
                fixed_message = fixMessage(i['message'], i['template'])
            s = parsed_provider["provider_name"] + "," + i["level"] + "," + i["eid"] + "," + i["version"] + "," + i["channel"] + "," + i["task"] + "," + i["opcode"] + "," + i["keyword"] + "," + fixed_message
            f.write(s)
            f.write("\n")
    convertCsvToMD(parsed_provider["provider_name"], folderName)

def merge_csv(folderName):
    header = "Provider,Level,Event ID,Version,Channel,Task,Opcode,Keyword,Message"
    path_to_csv_folder = "CSV/" + folderName + "/"
    listOfFile = os.listdir(path_to_csv_folder)
    listOfCsvs = list()
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(path_to_csv_folder, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            listOfCsvs = listOfCsvs + getListOfFiles(fullPath)
        else:
            listOfCsvs.append(fullPath) 
    
    with open("CSV/" + folderName + "/!All_" + folderName + "_ETW_Events.csv", "w+") as mergeall:
        mergeall.write(header)
        mergeall.write("\n")
        for csv in listOfCsvs:
            with open(csv, "r") as f:
                f.readline()
                all_lines = f.readlines()
                for i in all_lines:
                    mergeall.write(i)

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="providersPath", help="Path to the folder containing the ETW providers manifests")
    parser.add_option("-f", "--file", dest="providersFile", help="Path to an ETW manifest file")
    parser.add_option("-n", "--name", dest="folderName", help="Name for the folder that'll contain the results")
    (options, args) = parser.parse_args()
    if not options.providersPath:
        if not options.providersFile:
            parser.error("Please provide a valid path")
    elif options.providersFile:
        parser.error("Only one option can be chosen at a time")

    if not options.folderName:
        parser.error("Please provider a folder name")

    # Create seperate CSV and MD folders
    if not os.path.exists("CSV"):
        os.mkdir("CSV")
    else:
        print("CSV folder already exists")
    if not os.path.exists("Markdown"):
        os.mkdir("Markdown")
    else:
        print("Markdown folder already exists")

    # We collect the arguments from the user
    providersPath = options.providersPath
    providersFile = options.providersFile
    folderName = options.folderName

    if not os.path.exists("Markdown/" + folderName):
        os.mkdir("Markdown/" + folderName)
    else:
        os.rmdir("Markdown/" + folderName)
        os.mkdir("Markdown/" + folderName)

    if not os.path.exists("CSV/" + folderName):
        os.mkdir("CSV/" + folderName)
    else:
        os.rmdir("CSV/" + folderName)
        os.mkdir("CSV/" + folderName)

    if providersPath:
        # We call the "getListOfFiles" to generate a list of file paths
        listOfProviders = getListOfFiles(providersPath)
        listOfParsedProviders = []

        # We then parse and convert each file into a dict and append them to a list we call "list Of Parsed Providers"
        for provider in listOfProviders:
            parsed = parse_etw_xml(provider)
            if parsed != "Empty Provider":
                listOfParsedProviders.append(parsed)

        # We then start to generate the CSV file
        for p in listOfParsedProviders:
            converterStart(p, folderName)
        merge_csv(folderName)
    elif providersFile:
        parsed = parse_etw_xml(providersFile)
        if parsed == "Empty Provider":
            print("The provider manifest is empty. Nothing to convert")
        converterStart(parsed, folderName)
        merge_csv(folderName)