import os
import sys
from logic.constants.constants import *
from colorama import Fore, Style
from logic.md_csv_pdf_file import md_csv_pdf_file
from logic.generate_pdf import get_last_name
from dotenv import load_dotenv
load_dotenv()

md_file_path = os.getenv('PATH_MD')
csv_file_path = os.getenv('PATH_PROGRESS_CSV')

first_name = sys.argv[1]
name = get_last_name(f'{first_name.upper()}')
name = name.split(' ')[0]

name_index = os.getenv(f'{first_name.upper()}_INDEX')

selected_column_index = int(name_index)

print('\n')
print(Fore.GREEN + START_MESSAGE_PER.format(f'{name}') + Style.RESET_ALL)
print('\n')
print(Fore.YELLOW + f' 〉Markdown file loaded:   {md_file_path} ' + Style.RESET_ALL)
print('\n')

current_csv_file_path_template = os.getenv('PATH_CSV_LOOP')
current_csv_file_path = current_csv_file_path_template.replace('{i}', str(selected_column_index))
md_csv_pdf_file(md_file_path, current_csv_file_path, selected_column_index)

print('\n')
print(Fore.GREEN + DONE_MESSAGE_PER.format(f'{name}') + Style.RESET_ALL)
print('\n')


