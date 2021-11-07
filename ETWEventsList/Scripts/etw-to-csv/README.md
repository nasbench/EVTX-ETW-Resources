# ETW to CSV

## Output Example

![csvExample](csvExample.png)

## Requirements

```python
pip install csvtomd
```

## Usage

```python
Usage: etw-to-csv.py [options]

Options:
  -h, --help            show this help message and exit
  -p PROVIDERSPATH, --path=PROVIDERSPATH
                        Path to the folder containing the ETW providers
                        manifests
  -f PROVIDERSFILE, --file=PROVIDERSFILE
                        Path to an ETW manifest file
  -n FOLDERNAME, --name=FOLDERNAME
                        Name for the folder that'll contain the results
```

## Examples

- Generate CSVs / MDs from single file

```python
python etw-to-csv.py -f "/etw-providers/W10_20H2/WEPExplorer/Microsoft-Windows-Kernel-Process.xml" -n "W10_20H2"
```

- Generate CSVs / MDs from single file

```python
python etw-to-csv.py -p "/etw-providers/W10_20H2/WEPExplorer/" -n "W10_20H2"
```

## TODO

- [x] ~~Modify the script to be able to generate CSV and Markdown from a single ETW manifest instead of a folder.~~
- [x] ~~Add new parameter for file parsing and folder creation.~~
