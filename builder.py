import os
from logic.constants.constants import *
from colorama import Fore, Style
from logic.md_csv_pdf_file import md_csv_pdf_file
from dotenv import load_dotenv
load_dotenv()

md_file_path = os.getenv('PATH_MD')
csv_file_path = os.getenv('PATH_PROGRESS_CSV')

selected_column_index = 5

for i in range(4, 21):
    selected_column_index = i
    current_csv_file_path_template = os.getenv('PATH_CSV_LOOP')
    current_csv_file_path = current_csv_file_path_template.replace('{i}', str(i))
    md_csv_pdf_file(md_file_path, current_csv_file_path, selected_column_index)

print('\n')
print(Fore.GREEN + DONE_MESSAGE + Style.RESET_ALL)
print('\n')



