# CCCS Aventail IOC Extractor

This Python script is designed to extract Indicators of Compromise (IOCs) from data provided by the Canadian Centre for Cyber Security (CCCS) through Aventail.

## Description

The script reads a CSV file, processes it to extract unique data values, and writes these unique values to a text file. The unique values are determined based on the "Data Value/Valeur des données" column in the CSV file. The script also modifies the data value to strip characters after the third '/'. 

The output file is named in the format `CCCS-IOC-weeknumber.txt`, where `weeknumber` is the current week number. This allows for easy tracking and organization of IOCs on a weekly basis.

## Usage

To use this script, you need to provide the path to the input CSV file as a command line argument. Here's an example:

```bash
python3 CCCS-to-XDR.py -f /path/to/input.csv
