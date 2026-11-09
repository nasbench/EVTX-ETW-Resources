import argparse
import csv
import os
import re
import sys
from collections import defaultdict

import etwlib
from etwlib import EMPTY_PROVIDER, build_sort_key, fixMessage, parse_build_folder, parse_etw_xml, safe_filename

CSV_HEADER = ["Event ID", "Event Version", "Level", "Channel", "Task", "Opcode", "Keyword", "Windows", "Version", "Edition", "Date", "Build", "Event Message", "Event Fields"]
FIELD = re.compile(r"\{[A-Za-z0-9_]+\}")


def getProvidersPaths(etwdir_list):
    # {"Provider-Name": ["Path1", "Path2", "Path3".......]}
    # This is used to determine when an event was added or modified
    providers = defaultdict(list)
    for dirName in sorted(etwdir_list):
        for entry in sorted(os.listdir(dirName)):
            name, extension = os.path.splitext(entry)
            if entry != "All.xml" and extension == ".xml":
                providers[name].append(os.path.join(dirName, entry))
    return providers


def _number(text):
    try:
        return int(text)
    except ValueError:
        return 0


def createProvidersCSV(provider_dict, csvFolderName):
    os.makedirs("ETWProvidersCSVs/" + csvFolderName, exist_ok=True)
    for providerName, providersPaths in sorted(provider_dict.items()):
        print("Creating file for provider: " + str(providerName))
        rows = []
        for provider in providersPaths:
            parsedProvider = parse_etw_xml(provider)
            if parsedProvider == EMPTY_PROVIDER:
                continue
            if csvFolderName == "Internal":
                # We extract the Windows information from the build folder name
                # Example: ETWProvidersManifests/Windows10/1507/W10_1507_Pro_20150729_10240/WEPExplorer/Microsoft-Windows-Kernel-Process.xml
                info = parse_build_folder(os.path.basename(os.path.dirname(os.path.dirname(provider))))
            else:
                info = {"windows": "N/A", "version": "N/A", "edition": "N/A", "date": "N/A", "build": "N/A"}

            for eventInfo in parsedProvider["events"]:
                # Events without data fields have no template and no "%N" arguments
                fixed_message = eventInfo["message"]
                if eventInfo["template"] != "":
                    fixed_message = fixMessage(eventInfo["message"], eventInfo["template"])
                rows.append([
                    eventInfo["eid"], eventInfo["version"], eventInfo["level"], eventInfo["channel"],
                    eventInfo["task"], eventInfo["opcode"], eventInfo["keyword"],
                    info["windows"], info["version"], info["edition"], info["date"], info["build"],
                    fixed_message, " | ".join(FIELD.findall(fixed_message)),
                ])

        # Sort by event ID, then event version, then (internal providers only) newest build first.
        # Builds are compared as numbers: as text or as a float "26100.2" would sort above "26100.1742".
        # The sorts are stable, so sorting by build first keeps the builds ordered within an event.
        if csvFolderName == "Internal":
            rows.sort(key=lambda row: build_sort_key(row[11]), reverse=True)
        rows.sort(key=lambda row: (_number(row[0]), _number(row[1])))
        with open("ETWProvidersCSVs/" + csvFolderName + "/" + safe_filename(providerName) + ".csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(CSV_HEADER)
            writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the CSV of every ETW provider, over all Windows builds.")
    parser.add_argument(
        "--changed-since", metavar="REV",
        help="only generate the CSVs of the providers whose manifests changed between the git revision REV "
             "and HEAD (without it, every provider is generated)",
    )
    args = parser.parse_args()

    manifestsDir = "ETWProvidersManifests"
    etwdir, thirdParty_etwdir = [], []

    # This is used to extract the name of the folders containing the XML manifests
    for subdir, dirs, files in os.walk(manifestsDir):
        if "WEPExplorer" in str(subdir):
            etwdir.append(subdir)
        elif "ThirdParty" in str(subdir):
            thirdParty_etwdir.append(subdir)

    # Collect the available providers (Windows ones and third party ones) and every XML they have
    provider_dict = getProvidersPaths(etwdir)
    print("Internal Providers Dict READY")
    thrid_party_provider_dict = getProvidersPaths(thirdParty_etwdir)
    print("Third Party Providers Dict READY")
    if args.changed_since:
        # A provider CSV covers every build, so a changed manifest means that provider is generated again
        changed = etwlib.changed_provider_names(args.changed_since)
        provider_dict = {name: paths for name, paths in provider_dict.items() if name in changed}
        thrid_party_provider_dict = {name: paths for name, paths in thrid_party_provider_dict.items() if name in changed}
        print(f"{len(provider_dict) + len(thrid_party_provider_dict)} provider(s) changed since {args.changed_since}")

    # Now let's make a CSV per provider like this
    #---> Provider
    #Event ID | Version | Windows | Version | Build | Event Message        | Event Fields
    #1        | 0       | W10     | 1709    | XXXX  | Process Created...   | {ProcessID}
    #........
    # 1- We get the Windows information from the folder name
    # 2- We create a CSV file with the name of the provider, e.g. "Microsoft-Windows-Kernel-Process.csv"
    # 3- We parse the XML of every Windows version and add the events to the CSV
    # 4- We order the CSV by "Event ID + Event Version"
    createProvidersCSV(provider_dict, "Internal")
    createProvidersCSV(thrid_party_provider_dict, "ThirdParty")

    if etwlib.ERRORS:
        print(f"{len(etwlib.ERRORS)} manifest(s) could not be read:", file=sys.stderr)
        for error in etwlib.ERRORS:
            print("  " + error, file=sys.stderr)
        sys.exit(1)
