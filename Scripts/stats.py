import os
import xml.etree.ElementTree as ET
import csv
import re

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

        return events_list
    else:
        return "Empty Provider"

def getAllProvidersNameAvailable(etwdir_list):
    # We loop through each folder and collect the name and append it to the list
    allFiles = []
    for dirName in etwdir_list:
        listOfFile = os.listdir(dirName)
        for entry in listOfFile:
            if entry != "All.xml":
                if os.path.splitext(entry)[1] == ".xml":                    
                    allFiles.append(entry)
    # We use the "set" function to remove any duplicates
    return list(set(allFiles))

def searchProviderName(providerName, etwdir_list_fullpath):
    fullPathList = []
    for entry in etwdir_list_fullpath:
        if os.name == "nt":
            fileName = entry.split("\\")[-1]
        else:
            fileName = entry.split("/")[-1]
        if fileName != "All.xml":
            if os.path.splitext(fileName)[1] == ".xml":
                if fileName == providerName:
                    fullPathList.append(entry)
    return fullPathList

def createProvidersCSV(provider_dict, folderName):
    for providerName, providersPaths in provider_dict.items():
        print("Creating file for provider: " + str(providerName))
        print("ProviderName Type = " + str(type(providerName)))
        print("FolderName Type = " + str(type(folderName)))
        unsortedFileName = "ETWProvidersCSVs/"+ str(folderName) + "/" + str(providerName) + "_unsorted.csv"
        with open(unsortedFileName, "w") as f:
            # CSV HEADER
            f.write("Event ID,Event Version,Level,Channel,Task,Opcode,Keyword,Windows,Version,Edition,Date,Build,Event Message,Event Fields\n")
            for provider in providersPaths:
                parsedProvider = parse_etw_xml(provider)
                if parsedProvider != "Empty Provider":
                    # We will extract windows infom from the path for the "Internal" providers case
                    if folderName == "Internal":
                        if os.name == 'nt':
                            # We are splitting the provider name to get rid of the ".xml"
                            # Example => ETWProvidersManifests\\Windows10\\1507\\W10_1507_Pro_20150729_10240\\WEPExplorer\\Microsoft-Windows-Kernel-Process.xml
                            # We then split and extract the folder name
                            # Example would be: "W10_1507_Pro_20150729_10240"
                            folderName = os.path.splitext(provider)[0].split("\\")[:-2][-1].split("_")
                        else:
                            folderName = os.path.splitext(provider)[0].split("/")[:-2][-1].split("_")
                        # Example: Windows 10
                        if "WindowsServer" in folderName[0]:
                            windowsMajorVersion = "Windows Server " + folderName[0].split("WindowsServer")[1]
                        else:
                            windowsMajorVersion = "Windows " + folderName[0].split("W")[1]

                        # Example: 1903
                        windowsMinorVersion = folderName[1]

                        # Example: Pro/Entreprise
                        windowsEdition = folderName[2]

                        # Example: 205/07/29
                        windowsDate = folderName[3][0:4] + "/" + folderName[3][4:6] + "/" + folderName[3][6:8]

                        # Example: 10240
                        windowsBuild = folderName[4]

                    elif folderName == "ThirdParty":
                        windowsMajorVersion = "N/A"
                        windowsMinorVersion = "N/A"
                        windowsEdition = "N/A"
                        windowsDate = "N/A"
                        windowsBuild = "N/A"


                    for eventInfo in parsedProvider:
                        fixed_message = ""
                        if eventInfo['template'] != "":
                            fixed_message = fixMessage(eventInfo['message'], eventInfo['template'])
                        
                        eventLevel      = eventInfo["level"]
                        eventID         = eventInfo["eid"]
                        eventVersion    = eventInfo["version"]
                        eventChannel    = eventInfo["channel"]
                        eventTask       = eventInfo["task"]
                        eventOpcode     = eventInfo["opcode"]
                        eventKeyword    = eventInfo["keyword"]
                        eventMessage    = fixed_message
                        eventFields     = " | ".join(re.findall("{[a-zA-z0-9]*}",fixed_message))

                        f.write(
                            eventID + "," + 
                            eventVersion + "," + 
                            eventLevel + "," + 
                            eventChannel + "," +
                            eventTask + "," +  
                            eventOpcode + "," + 
                            eventKeyword + "," + 
                            windowsMajorVersion + "," + 
                            windowsMinorVersion + "," + 
                            windowsEdition + "," + 
                            windowsDate + "," + 
                            windowsBuild + "," + 
                            eventMessage + "," + 
                            eventFields + "\n"
                        )
        
        # We then sort the data first by EID and then by Event Version and write it to a new file
        unsorted_file = open(unsortedFileName)
        reader = csv.reader(unsorted_file, delimiter=",")
        with open(unsortedFileName.replace("_unsorted.csv", ".csv"), "w") as f:
            f.write("Event ID,Event Version,Level,Channel,Task,Opcode,Keyword,Windows,Version,Edition,Date,Build,Event Message,Event Fields\n")
            for sortedData in sorted(reader, key=lambda row:(row[0],row[1]), reverse=False)[:-1]:
                f.write(",".join(sortedData))
                f.write("\n")
        
        # We remove the unsorted data
        unsorted_file.close()
        os.remove(unsortedFileName)

if __name__=="__main__":
    manifestsDir = "ETWProvidersManifests"
    etwdir, etwdir_fullPaths, thirdParty_etwdir, thirdParty_etwdir_fullPaths = [], [], [], []

    # This is used to extract the name of the folders containing the XML manifests
    for subdir, dirs, files in os.walk(manifestsDir):
        if "WEPExplorer" in str(subdir):
            etwdir.append(subdir)
            for singleFile in files:
                if os.name == 'nt':
                    etwdir_fullPaths.append(subdir + "\\" + singleFile)
                else:
                    etwdir_fullPaths.append(subdir + "/" + singleFile)
        elif "ThirdParty" in str(subdir):
            thirdParty_etwdir.append(subdir)
            for singleFile in files:
                if os.name == 'nt':
                    thirdParty_etwdir_fullPaths.append(subdir + "\\" + singleFile)
                else:
                    thirdParty_etwdir_fullPaths.append(subdir + "/" + singleFile)

    # We call "getAllProvidersNameAvailable" to collect all the available provider names for both Windows providers and thrid party ones
    all_providers_names = getAllProvidersNameAvailable(etwdir)
    thrid_party_providers_names = getAllProvidersNameAvailable(thirdParty_etwdir)

    # We now loop on every name and search every XML folder and create a dict similar to the following structure
    # {"ProvideName": ["Path1", "Path2", "Path3".......]}
    # This will be used to determine when an event was added or modified

    # We do this for internal providers
    provider_dict = {}
    for i in all_providers_names:
        provider_dict[os.path.splitext(i)[0]] = searchProviderName(i, etwdir_fullPaths)
    print("Internal Providers Dict READY")

    # We do the same for third party providers
    thrid_party_provider_dict = {}
    for i in thrid_party_providers_names:
        thrid_party_provider_dict[os.path.splitext(i)[0]] = searchProviderName(i, thirdParty_etwdir_fullPaths)
    print("Third Party Providers Dict READY")

    # Now let's make a CSV like this
    #---> Provider
    #Event ID | Version | Windows | Version | Build | Available | Updated | Original Message     | Added Fields
    #1        | 0       | W10     | 1709    | XXXX  | Yes       | No      | Process Created...   | N/A
    #1        | 1       | W10     | 1803    | XXXX  | Yes       | No      | N/A                  | New Field
    #........

    # 1- We can get Windows information form the folder name
    # 2- We will create a CSV file with the name of the key. So for example => "Microsoft-Windows-Kernel-Process.csv"
    # 3- We will parse every XML for every version and extract the necessary information and add it to the CSV
    # 4- Order the CSV by "EVENT ID + EVENT VERSION"

    # We create the CSVs by calling the "createProvidersCSV" function for both default providers and 3rd party ones
    # Header: createProvidersCSV(provider_dict, foldername):
    # provider_dict => Contains the default windows provider
    # thrid_party_provider_dict => Contains the 3rd party providers
    createProvidersCSV(provider_dict, "Internal")
    createProvidersCSV(thrid_party_provider_dict, "ThirdParty")