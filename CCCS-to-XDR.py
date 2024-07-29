import csv
import re
import argparse
from datetime import datetime

# Define a function to clean up URLs and domains
def clean_url_or_domain(value):
    # Remove the scheme (http, https)
    value = re.sub(r'^https?:\/\/', '', value)
    # Remove subdirectories
    value = re.sub(r'\/.*', '', value)
    return value

# Define a function to process the CSV file
def process_csv(input_file):
    # Define the allowed data types
    allowed_data_types = ["URL/URL", "IP_ADDRESS/ADRESSE_IP", "DOMAIN/DOMAINE", "MD5/MD5"]
    
    # Read the input CSV file
    with open(input_file, mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        # Skip the first three rows
        for _ in range(3):
            next(reader)
        
        # Process the remaining rows
        processed_data = set()
        for row in reader:
            if len(row) < 2:
                continue  # Skip rows that don't have at least two columns
            data_type, data_value = row[0], row[1]
            if data_type in allowed_data_types:
                if data_type in ["URL/URL", "DOMAIN/DOMAINE"]:
                    data_value = clean_url_or_domain(data_value)
                processed_data.add(data_value)
    
    # Get the current week number
    week_number = datetime.now().isocalendar()[1]
    output_file = f'cccs-ioc-week{week_number}.txt'
    
    # Write the processed data to the output file
    with open(output_file, mode='w', encoding='utf-8') as file:
        for data_value in processed_data:
            file.write(data_value + '\n')
    
    print(f'Processed data has been saved to {output_file}')

# Define the main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('-f', '--file', required=True, help='Path to the input CSV file')
    args = parser.parse_args()
    process_csv(args.file)

if __name__ == '__main__':
    main()
