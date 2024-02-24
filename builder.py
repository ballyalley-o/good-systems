import os
from logic.constants.constants import *
from colorama import Fore, Style
from logic.md_csv_pdf_file import md_csv_pdf_file
from dotenv import load_dotenv
load_dotenv()

md_file_path = os.getenv('PATH_MD')
csv_file_path = os.getenv('PATH_PROGRESS_CSV')

selected_column_index = 5

print('\n')
print(Fore.GREEN + START_MESSAGE + Style.RESET_ALL)
print('\n')
print(Fore.YELLOW + f' 〉Markdown file loaded:   {md_file_path} ' + Style.RESET_ALL)
print('\n')

for i in range(3, 21):
    selected_column_index = i
    current_csv_file_path_template = os.getenv('PATH_CSV_LOOP')
    current_csv_file_path = current_csv_file_path_template.replace('{i}', str(i))
    md_csv_pdf_file(md_file_path, current_csv_file_path, selected_column_index)

# TODO: logic for adding all the content in converting the progress-all.csv to a md file
    # - get that md content and paste it on IODPROGRESS.md

# TODO: convert the progress-all.csv and save it as markdown file to gist/progress.md
# TODO: email pdfs to students
# TODO: special bgs in the mini-project row for students who are top 3 in the miniproject

print('\n')
print(Fore.GREEN + DONE_MESSAGE + Style.RESET_ALL)
print('\n')



