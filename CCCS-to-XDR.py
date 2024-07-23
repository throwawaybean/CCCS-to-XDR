import argparse
import csv
from datetime import datetime

def parse_csv(input_file):
    # Initialize a set to store unique data values
    unique_values = set()

    # Open the CSV file for reading
    with open(input_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        
        # Skip the first three rows
        for _ in range(3):
            next(reader)
        
        # Initialize column indices
        data_type_index = -1
        data_value_index = -1
        
        # Read the header row to determine column indices
        header = next(reader)
        for index, column in enumerate(header):
            if "Data Type/Type de données" in column:
                data_type_index = index
            elif "Data Value/Valeur des données" in column:
                data_value_index = index
        
        # If "Data Value/Valeur des données" column not found, default to second column
        if data_value_index == -1:
            data_value_index = 1
        
        # Process each row in the CSV
        for row in reader:
            if len(row) > data_value_index and row[data_value_index].strip():
                # Modify the data value to strip characters after the third '/'
                data_value = row[data_value_index].strip()
                # Find the third '/' and slice up to that point
                third_slash_index = data_value.find('/', data_value.find('/', data_value.find('/') + 1) + 1)
                if third_slash_index != -1:
                    data_value = data_value[:third_slash_index]

                # Add the modified data value to the set (to ensure uniqueness)
                unique_values.add(data_value.strip())
    
    # Get the current week number
    week_number = datetime.now().isocalendar()[1]

    # Define the output file name
    output_file = f'CCCS-IOC-week{week_number}.txt'

    # Write unique values to a text file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for value in sorted(unique_values):
            outfile.write(value + '\n')

    # Print a success message
    print(f"The file has been saved as {output_file}")

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process CSV file and extract unique data values.')
    parser.add_argument('-f', '--file', required=True, help='Input CSV file path')
    args = parser.parse_args()
    
    # Call function to parse the CSV file
    parse_csv(args.file)

