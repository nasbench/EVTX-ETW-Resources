from collections import Counter
import csv
import os
import sys

import csvtomd
import pandas as pd

import etwlib
from etwlib import EMPTY_PROVIDER, fixMessage, parse_etw_xml, safe_filename

HEADER = ["Provider", "Level", "Event ID", "Version", "Channel", "Task", "Opcode", "Keyword", "Message"]

# This is a special version related to generating STATS
def convertCsvToMDStats(folderName, windowsName, version, edition, date, build):
    csvReadme = folderName + "/README.csv"
    with open(csvReadme, "r") as f:
        table = csvtomd.csv_to_table(f, ",")
    
    if table:
        with open(folderName + "/README.md", "w") as f:
            f.write("# " + windowsName + " " + edition + " " + version  + " (Date: " + date + " - " + "Build: " + build + ") - ETW Providers\n\n")
            f.write(csvtomd.md_table(table, padding=2))
        os.remove(csvReadme)
    else:
        print("Cannot Convert to Markdown")

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = sorted(os.listdir(dirName))
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
    path_to_csv_folder = csvDir + folderToCreate + "Providers"
    listOfCsvs = [os.path.join(path_to_csv_folder, entry) for entry in sorted(os.listdir(path_to_csv_folder))]

    folderName = folderToCreate[:-1]
    folderName = folderName[folderName.rfind("/"):].replace("/", "")
    with open(csvDir + folderToCreate + "!All_" + folderName + "_ETW_Events.csv", "w", newline="", encoding="utf-8") as mergeall:
        writer = csv.writer(mergeall, lineterminator="\n")
        writer.writerow(HEADER)
        for providerCsv in listOfCsvs:
            with open(providerCsv, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)
                writer.writerows(reader)

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
        with open(i, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            allevents = list(reader)
            numOfEvents = len(allevents)
            folderName = os.path.dirname(i)            
                
            with open(folderName + "/README.csv", "w", newline="", encoding="utf-8") as ff:
                writer = csv.writer(ff, lineterminator="\n")
                writer.writerow(["ETW Provider", "Number Of Events"])
                for provider, count in Counter([event[0] for event in allevents]).most_common():
                    writer.writerow([provider, count])
                    numOfProviders += 1

            convertCsvToMDStats(folderName, windowsName, version, edition, date, build)

            #numOfProviders = len(Counter([i.split(",")[0] for i in allevents ]))
        final_restls.append(windowsName + "," + edition + "," + version + "," + date + "," + build + "," + str(numOfProviders) + "," + str(numOfEvents))

    with open("ETWEventsList/etw-stats-unsorted.csv", "w") as f:
            f.write("Windows,Edition/SP,Version,Date,Build,Num Providers,Num Events\n")
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

def converterStart(parsed_provider, folderToCreate, csvDir, usedNames):
    # "TCP/IP" cannot be a file name, and names that only differ by case must not collide
    name = safe_filename(parsed_provider["provider_name"])
    candidate, suffix = name, 1
    while candidate.lower() in usedNames:
        suffix += 1
        candidate = f"{name}_{suffix}"
    usedNames.add(candidate.lower())

    with open(csvDir + folderToCreate + "Providers/" + candidate + ".csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(HEADER)
        for i in parsed_provider["events"]:
            fixed_message = fixMessage(i["message"], i["template"]) if i["template"] else i["message"]
            writer.writerow([parsed_provider["provider_name"], i["level"], i["eid"], i["version"], i["channel"], i["task"], i["opcode"], i["keyword"], fixed_message])

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
            if parsed != EMPTY_PROVIDER:
                listOfParsedProviders.append(parsed)

        # Create directories
        if os.path.exists(csvDir + folderToCreate):
            print(csvDir + folderToCreate + " - Already exists")
        os.makedirs(csvDir + folderToCreate + "Providers", exist_ok=True)

        # We then start to generate the CSV files
        usedNames = set()
        for p in listOfParsedProviders:
            converterStart(p, folderToCreate, csvDir, usedNames)
        merge_csv(folderToCreate, csvDir)
        generateStats()

    if etwlib.ERRORS:
        print(f"{len(etwlib.ERRORS)} manifest(s) could not be read:", file=sys.stderr)
        for error in etwlib.ERRORS:
            print("  " + error, file=sys.stderr)
        sys.exit(1)