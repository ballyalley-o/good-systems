import csv
import os
import sys
from dotenv import load_dotenv
load_dotenv()

def csv_to_md(csv_file_path, md_file_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        data = list(reader)

    with open(md_file_path, 'w') as md_file:
        md_file.write('| ' + ' | '.join(headers) + ' |\n')
        md_file.write('| ' + ' | '.join(['---']*len(headers)) + ' |\n')
        for row in data:
            md_file.write('| ' + ' | '.join(row) + ' |\n')

    print(f' File {csv_file_path} has been CONVERTED to {md_file_path}')

csv_file_path = os.getenv('PATH_ALL_CSV')
md_file_path = os.getenv('PATH_MD')

# md_file_path = os.getenv('PATH_TEST_MD')
# csv_file_path = os.getenv('PATH_TEST_CSV')
csv_to_md(csv_file_path, md_file_path)
