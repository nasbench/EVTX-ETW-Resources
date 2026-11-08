import csv
import os
import sys
from collections import Counter

import etwlib
from etwlib import EMPTY_PROVIDER, fixMessage, md_table, parse_build_folder, parse_etw_xml, safe_filename

HEADER = ["Provider", "Level", "Event ID", "Version", "Channel", "Task", "Opcode", "Keyword", "Message"]
STATS_HEADER = ["Windows", "Edition/SP", "Version", "Date", "Build", "Num Providers", "Num Providers With Events", "Num Events"]
CSV_DIR = "ETWEventsList/CSV/"
STATS_CSV = "ETWEventsList/etw-global-stats.csv"


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


def build_stats(allEventsCsv):
    """Write the README.md of a build folder and return its row of the global stats."""
    folder = os.path.dirname(allEventsCsv)
    info = parse_build_folder(os.path.basename(allEventsCsv).replace("!All_", "").replace("_ETW_Events.csv", ""))

    eventsPerProvider = Counter()
    with open(allEventsCsv, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            eventsPerProvider[row[0]] += 1
    numOfEvents = sum(eventsPerProvider.values())
    # Every provider with event metadata has a CSV, including those without events
    numOfProviders = len(os.listdir(folder + "/Providers"))

    table = [["ETW Provider", "Number Of Events"]]
    for provider, count in sorted(eventsPerProvider.items(), key=lambda item: (-item[1], item[0])):
        table.append([provider, str(count)])
    with open(folder + "/README.md", "w", encoding="utf-8") as f:
        f.write("# " + info["windows"] + " " + info["edition"] + " " + info["version"] + " (Date: " + info["date"] + " - " + "Build: " + info["build"] + ") - ETW Providers\n\n")
        f.write(md_table(table, padding=2))

    return [info["windows"], info["edition"], info["version"], info["date"], info["build"], str(numOfProviders), str(len(eventsPerProvider)), str(numOfEvents)]


def write_global_stats(rows):
    # Most providers first, then most events
    rows = sorted(rows, key=lambda row: (-int(row[5]), -int(row[7]), row[:5]))
    with open(STATS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(STATS_HEADER)
        writer.writerows(rows)

    with open("ETWEventsList/README.md", "w", encoding="utf-8") as f:
        f.write("# ETW Events List\n\n")
        f.write("The following folder contains a list of all ETW events extracted from the currently dumped ETW manifests (See [**ETW Providers Manifests**](https://github.com/nasbench/ETW-Resources/tree/main/ETWProvidersManifests) for the complete list).\n\n")
        f.write("`Num Providers` counts the manifests that have event metadata, `Num Providers With Events` those that define at least one event.\n\n")
        f.write("## Global ETW Stats\n")
        f.write(md_table([STATS_HEADER] + rows, padding=2))


def generateStats():
    listOfAllFiles = []
    for (dirpath, dirnames, filenames) in os.walk(CSV_DIR):
        for i in filenames:
            if i.startswith("!"):
                listOfAllFiles.append(dirpath + "/" + i)
    write_global_stats([build_stats(i) for i in sorted(listOfAllFiles)])


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


if __name__ == "__main__":
    manifestsDir = "ETWProvidersManifests"
    etwdir = []

    # This is used to extract the name of the folders
    for subdir, dirs, files in os.walk(manifestsDir):
        if "WEPExplorer" in str(subdir):
            etwdir.append(subdir)

    for i in sorted(etwdir):
        # This will get the name of the folder/subfolders to create in order to replicate the same structure as the XML's
        folderToCreate = i[i.find("ETWProvidersManifests") + len("ETWProvidersManifests") + 1:].replace("WEPExplorer", "").replace("\\", "/")
        # We call the "getListOfFiles" to generate a list of file paths
        listOfProviders = getListOfFiles(i)
        listOfParsedProviders = []

        # We then parse and convert each file into a dict and append them to a list we call "list Of Parsed Providers"
        for provider in listOfProviders:
            parsed = parse_etw_xml(provider)
            if parsed != EMPTY_PROVIDER:
                listOfParsedProviders.append(parsed)

        # Create directories
        if os.path.exists(CSV_DIR + folderToCreate):
            print(CSV_DIR + folderToCreate + " - Already exists")
        os.makedirs(CSV_DIR + folderToCreate + "Providers", exist_ok=True)

        # We then start to generate the CSV files
        usedNames = set()
        for p in listOfParsedProviders:
            converterStart(p, folderToCreate, CSV_DIR, usedNames)
        merge_csv(folderToCreate, CSV_DIR)

    generateStats()

    if etwlib.ERRORS:
        print(f"{len(etwlib.ERRORS)} manifest(s) could not be read:", file=sys.stderr)
        for error in etwlib.ERRORS:
            print("  " + error, file=sys.stderr)
        sys.exit(1)
