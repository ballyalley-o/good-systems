import csv
import os
from colorama import Fore, Style, Back
from dotenv import load_dotenv
load_dotenv()

def md_to_csv(md_table):
    md_table = md_table.replace('```', '')
    md_table = md_table.replace('**', '')

    lines = md_table.split('\n')
    lines = lines[:1] + lines[2:]

    csv_lines = []

    for line in lines:
        values = line.split('|')
        values = [v.strip() for v in values]
        csv_lines.append(values)

    return csv_lines

def md_to_csv_file(md_file_path, csv_file_path):
    with open(md_file_path, 'r') as file:
        md_table = file.read()

    csv_data = md_to_csv(md_table)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(Back.BLUE + Fore.WHITE + f' 〉Legend CSV file saved: {csv_file_path}' + Style.RESET_ALL)

# File paths
md_file_path = os.getenv('PATH_LEGEND_MD')
csv_file_path = os.getenv('PATH_LEGEND_CSV')

md_to_csv_file(md_file_path, csv_file_path)
