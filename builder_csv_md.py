import csv
import os
import re
import datetime
from colorama import Fore, Style
from logic.constants.constants import *
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

    with open(md_file_path, 'r') as md_file:
        md_file_content = md_file.read()
        md_file_content = md_file_content.split('\n')
        md_file_content = '\n'.join(md_file_content[2:])


def replace_content(original_file_path, md_file_path, legend_file_path):
    # Read the original file
    with open(original_file_path, 'r') as file:
        original_content = file.read()

    with open(md_file_path, 'r') as file:
        md_content = file.read()

    with open(legend_file_path, 'r') as file:
        legend_content = file.read()

    now = datetime.datetime.now()
    new_date = now.strftime("%d%b%H:%M").upper()
    original_content = re.sub(r'(\d{2}[A-Z]{3}\d{2}:\d{2})(-blue)', new_date + r'\2', original_content)


    start_index = original_content.find(GIST_CUTOFF_ST_MARKER)
    end_index = original_content.find(GIST_CUTOFF_END_MARKER)

    legend_start_index = original_content.find(GIST_LEGEND_CUTOFF_ST_MARKER)
    legend_end_index = original_content.find(GIST_LEGEND_CUTOFF_END_MARKER)

    if start_index == -1 or end_index == -1 or legend_start_index == -1 or legend_end_index == -1:
        print(f"{Fore.RED} {MARKER_NOT_FOUND} {Style.RESET_ALL}")
        return

    new_content = original_content[:start_index + len(GIST_CUTOFF_ST_MARKER)] + '\n' + md_content + '\n' + original_content[end_index:]
    new_content_with_legend = original_content[:legend_start_index + len(GIST_LEGEND_CUTOFF_ST_MARKER)] + '\n' + legend_content + '\n' + original_content[legend_end_index:]

    with open(original_file_path, 'w') as file:
        file.write(new_content)

    with open(original_file_path, 'w') as file:
        file.write(new_content_with_legend)

    print(f' ▶︎ {Fore.GREEN} {CONVERTED_MSG} {Style.RESET_ALL}')
    print('\n')
    print(f'{Fore.YELLOW} {GIST_UPDATED_MSG} {Style.RESET_ALL}')


csv_file_path = os.getenv('PATH_ALL_CSV')
md_file_path = os.getenv('PATH_MD')
gist_file_path = os.getenv('PATH_GIST_MD')
legend_file_path = os.getenv('PATH_LEGEND_MD')

# for debugging !DON'T DELETE!
# md_file_path = os.getenv('PATH_TEST_MD')
# legend_file_path = os.getenv('PATH_LEGEND_MD')
# gist_file_path = os.getenv('PATH_GIST_TEST_MD')
# csv_file_path = os.getenv('PATH_TEST_CSV')

csv_to_md(csv_file_path, md_file_path)
replace_content(gist_file_path, md_file_path,legend_file_path)

