# 4.Implement a program to read a CSV file and display its contents in a tabular format.

import csv
from tabulate import tabulate

def read_and_display_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the first row as header
            rows = [row for row in reader]

            print("\nCSV File Contents in Tabular Format:\n")
            print(tabulate(rows, headers=headers, tablefmt='grid'))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the CSV file name (e.g., data.csv): ").strip()
    read_and_display_csv(file_path)
