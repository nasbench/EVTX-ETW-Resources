import xml.etree.ElementTree as ET
from collections import Counter
import os
import csvtomd
import csv
import pandas as pd

# This is a special version related to generating STATS
def convertCsvToMDStats(folderName, windowsName, version, edition, date, build):
    csvReadme = folderName + "/README.csv"
    with open(csvReadme, "r") as f:
        table = csvtomd.csv_to_table(f, ",")
    
    if table:
        with open(folderName + "/README.md", "w") as f:
            f.write("# " + windowsName + " " + edition + " " + version  + "(Date: " + date + " - " + "Build: " + build + ") - ETW Providers\n\n")
            f.write(csvtomd.md_table(table, padding=2))
        os.remove(csvReadme)
    else:
        print("Cannot Convert to Markdown")

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

def merge_csv(folderToCreate, csvDir):
    header = "Provider,Level,Event ID,Version,Channel,Task,Opcode,Keyword,Message"
    path_to_csv_folder = csvDir + folderToCreate + "Providers"
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
    
    folderName = folderToCreate[:-1]
    folderName = folderName[folderName.rfind("/"):].replace("/", "")
    with open(csvDir + folderToCreate + "!All_" + folderName + "_ETW_Events.csv", "w+") as mergeall:
        mergeall.write(header)
        mergeall.write("\n")
        for csv in listOfCsvs:
            with open(csv, "r") as f:
                f.readline()
                all_lines = f.readlines()
                for i in all_lines:
                    mergeall.write(i)

def getNumberOfEventsPerVersion(listOfAllFiles):
    final_restls = []
    for i in listOfAllFiles:

        fullName = os.path.basename(i).replace("!All_", "").replace("_ETW_Events.csv", "").split("_")
        if "WindowsServer" in fullName[0]:
            windowsName = "Windows Server " + fullName[0].split("WindowsServer")[1]
        else:
            windowsName = "Windows " + fullName[0].split("W")[1]
        version = fullName[1]
        edition = fullName[2]
        try:
            date = fullName[3][0:4] + "/" + fullName[3][4:6] + "/" + fullName[3][6:8]
        except:
            date = ""
        try:
            build = fullName[4]
        except:
            build = ""

        numOfProviders = 0
        with open(i, "r") as f:
            f.readline()
            allevents = f.readlines()
            numOfEvents = len(allevents)
            folderName = os.path.dirname(i)            
                
            with open(folderName + "/README.csv", "w") as ff:
                ff.write("ETW Provider,Number Of Events\n")
                for i in Counter([i.split(",")[0] for i in allevents]).most_common():
                    ff.write(i[0] + "," + str(i[1]))
                    numOfProviders += 1
                    ff.write("\n")

            convertCsvToMDStats(folderName, windowsName, version, edition, date, build)

            #numOfProviders = len(Counter([i.split(",")[0] for i in allevents ]))
        final_restls.append(windowsName + "," + edition + "," + version + "," + date + "," + build + "," + str(numOfProviders) + "," + str(numOfEvents))

    with open("ETWEventsList/etw-stats-unsorted.csv", "w") as f:
            f.write("Windows,Edition/SP,Version,Date,Build,Num Providers, Num Events\n")
            for i in final_restls:
                f.write(i)
                f.write("\n")
    # Let's sort the created file by "Num Of Providers"
    csvdata = pd.read_csv("ETWEventsList/etw-stats-unsorted.csv")
    csvdata.sort_values(["Num Providers", "Num Events"], axis=0, ascending=[False, False], inplace=True)
    csvdata.to_csv("ETWEventsList/etw-global-stats.csv", encoding='utf-8', index=False)
    os.remove("ETWEventsList/etw-stats-unsorted.csv")

    # Convert Results to MD
    with open("ETWEventsList/etw-global-stats.csv", "r") as f:
        table = csvtomd.csv_to_table(f, ",")
    with open("ETWEventsList/README.md", "w") as f:
        f.write("# ETW Events List\n\n")
        f.write("The following folder contains a list of all ETW events extracted from the currently dumped ETW manifests (See [**ETW Providers Manifests**](https://github.com/nasbench/ETW-Resources/tree/main/ETWProvidersManifests) for the complete list).\n\n")
        f.write("## Global ETW Stats\n")
        f.write(csvtomd.md_table(table, padding=2))

def generateStats():
    listOfAllFiles = []
    for (dirpath, dirnames, filenames) in os.walk("ETWEventsList/CSV/"):
        for i in filenames:
            if i.startswith("!"):
                listOfAllFiles.append(dirpath + "/" + i)
    getNumberOfEventsPerVersion(listOfAllFiles)

def converterStart(parsed_provider, folderToCreate, csvDir):
    header = "Provider,Level,Event ID,Version,Channel,Task,Opcode,Keyword,Message"
    with open(csvDir + folderToCreate + "/Providers/" + parsed_provider["provider_name"] + ".csv", "w+") as f:
        f.seek(0)
        f.write(header)
        f.write("\n")
        for i in parsed_provider["events"]:
            fixed_message = ""
            if i['template'] != "":
                fixed_message = fixMessage(i['message'], i['template'])
            s = parsed_provider["provider_name"] + "," + i["level"] + "," + i["eid"] + "," + i["version"] + "," + i["channel"] + "," + i["task"] + "," + i["opcode"] + "," + i["keyword"] + "," + fixed_message
            f.write(s)
            f.write("\n")
    #print(csvDir + folderToCreate + "/Providers/" + parsed_provider["provider_name"] + ".csv - Has been written")

if __name__=="__main__":
    manifestsDir = "ETWProvidersManifests"
    csvDir = "ETWEventsList/CSV/"
    etwdir = []

    # This is used to extract the name of the folders
    for subdir, dirs, files in os.walk(manifestsDir):
        if "WEPExplorer" in str(subdir): 
            etwdir.append(subdir)
            
    for i in etwdir:
        # This will get the name of the folder/subfolders to create in order to replicate the same structure as the XML's
        folderToCreate = i[i.find("ETWProvidersManifests")+len("ETWProvidersManifests")+1:].replace("WEPExplorer", "").replace("\\", "/")
        # We call the "getListOfFiles" to generate a list of file paths
        listOfProviders = getListOfFiles(i)
        listOfParsedProviders = []

        # We then parse and convert each file into a dict and append them to a list we call "list Of Parsed Providers"
        for provider in listOfProviders:
            parsed = parse_etw_xml(provider)
            if parsed != "Empty Provider":
                listOfParsedProviders.append(parsed)

        # Create directories
        if not os.path.exists(csvDir + folderToCreate):
            os.makedirs(csvDir + folderToCreate + "Providers")
        else:
            print(csvDir + folderToCreate + " - Already exists")

        # We then start to generate the CSV files
        for p in listOfParsedProviders:
            converterStart(p, folderToCreate, csvDir)
        merge_csv(folderToCreate, csvDir)
        generateStats()