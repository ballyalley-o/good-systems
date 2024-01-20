import os
import sys
from logic.constants.constants import *
from colorama import Fore, Style
from logic.md_csv_pdf_file import md_csv_pdf_file
from logic.generate_pdf import get_last_name
from dotenv import load_dotenv
load_dotenv()

def generate_progress_report():
    """
    Generates a progress report for a specific student.

    This function takes the first name of a student as a command line argument and generates a progress report for that student.
    It loads the necessary environment variables, retrieves the markdown file path and CSV file path from the environment variables, and gets the last name of the student.
    It then retrieves the index of the selected student's column from the environment variables.
    The function prints a start message, loads the markdown file, and generates a PDF file using the markdown and CSV files.
    Finally, it prints a done message indicating the completion of the progress report generation.

    Args:
        None

    Returns:
        None
    """
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

generate_progress_report()
