# ETW Events List

The following folder contains a list of all ETW events extracted from the currently dumped ETW manifests (See [**ETW Providers Manifests**](https://github.com/nasbench/ETW-Resources/tree/main/ETW%20Providers%20Manifests) for the complete list).

![csvExample](https://github.com/nasbench/ETW-Resources/tree/main/ETW%20Events%20List/csvExample.png)

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
  -n FILENAME, --name=FILENAME
                        Name of the to be generated file without extension
```

Here is an example on how to use the script

```python
python etw-to-csv.py -p /home/lab/etw-providers/w10_20h2 -n w10_20h2
```

**Note** that the script can convert the generated **`CSV`** file into **`Markdown`**. We just need to uncomment the last line.

```python
convertToMD(fileName)
```

## TODO

1- Modify the script to be able to generate CSV and Markdown from a single ETW manifest instead of a folder.
