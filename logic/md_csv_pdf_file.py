import csv
import os
from colorama import Fore, Back, Style
from .md_csv import md_to_csv
from .generate_pdf import generate_pdf

def md_csv_pdf_file(md_file_path, csv_file_path, selected_column_index):
    """
    Convert a Markdown file to CSV, save the CSV file, and generate a PDF file. for ALL Students

    Args:
        md_file_path (str): The file path of the Markdown file.
        csv_file_path (str): The file path to save the CSV file.
        selected_column_index (int): The index of the column to select from the Markdown table.

    Returns:
        None
    """
    with open(md_file_path, 'r') as file:
        md_table = file.read()

    csv_table, student_table = md_to_csv(md_table, selected_column_index)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        rows = [row.split(',') for row in csv_table.split('\n')]
        writer.writerows(rows)

    student_table_str = '\n'.join(student_table)

    output_file_name = rows[0][2]

    selected_file_path_template = os.getenv('PATH_CSV_SELECT')
    selected_file_path = selected_file_path_template.replace('{output_file_name}', output_file_name)

    with open(selected_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        rows = [row.split(',') for row in student_table_str.split('\n')]
        writer.writerows(rows)

    generate_pdf(md_csv_pdf_file, selected_file_path, output_file_name)

    print(Back.GREEN + Fore.WHITE + f' 〉CSV file saved:  {csv_file_path} ' + Style.RESET_ALL)
    print(Fore.YELLOW + f' 〉{output_file_name}\'s record saved:  {selected_file_path} ' + Style.RESET_ALL)
    print(Back.RED + Fore.YELLOW + f' 〉PDF file generated: {output_file_name}.pdf ' + Style.RESET_ALL)