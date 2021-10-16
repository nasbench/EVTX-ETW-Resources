# ETW Events List

The following folder contains a list of all ETW events extracted from the currently dumped ETW manifests (See [**ETW Providers Manifests**](https://github.com/nasbench/ETW-Resources/tree/main/ETW%20Providers%20Manifests) for the complete list).

![csvExample](csvExample.png)

The CSV/Markdown files were generated using the script **[etw-to-csv.py](https://github.com/nasbench/ETW-Resources/tree/main/ETW%20Events%20List/etw-to-csv.py)**.

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
```

Here is an example on how to use the script

```python
python etw-to-csv.py -p /home/lab/etw-providers/w10_20h2
```

The script will generates both a **`CSV`** and a **`Markdown`** version for each ETW Manifest.

```python
convertCsvToMD(fileName)
```

## TODO

- [x] ~~Modify the script to be able to generate CSV and Markdown from a single ETW manifest instead of a folder.~~
