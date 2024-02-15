import csv
import os
from colorama import Fore, Style
from dotenv import load_dotenv
load_dotenv()


def md_to_csv(md_table):
    md_table = md_table.replace('```', '')
    md_table = md_table.replace('**', '')

    lines = md_table.split('\n')

    exclude = os.getenv('EXCLUDE')

    lines = [lines[0]] + [line for line in lines[1:] if exclude not in line]

    # lines = lines[:1] + lines[2:]

    lines = [line.strip() for line in lines if line]

    header = [value.strip() for value in lines[0].split('|') if value]
    data = [line.split('|') for line in lines[2:]]

    csv_lines = []

    for values in data:
        values = [value.strip() for value in values if value]
        csv_lines.append(values)

    return header, csv_lines

def md_to_csv_file(md_file_path, csv_file_path):
    with open(md_file_path, 'r') as file:
        md_table = file.read()

    header, csv_lines = md_to_csv(md_table)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(csv_lines)

    print('\n')
    print(Fore.YELLOW + f' 🏆 All Students Progress CSV file saved to {csv_file_path} '  + Style.RESET_ALL)
    print('\n')

    # TODO: SMPT email fro sending the csv file to the students. CHECK smpt-students.py



md_file_path = os.getenv('PATH_ALL_MD')
csv_file_path = os.getenv('PATH_ALL_CSV')

md_to_csv_file(md_file_path, csv_file_path)
