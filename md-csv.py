import csv
import os
from colorama import Fore, Style, Back
from dotenv import load_dotenv
load_dotenv()

def md_to_csv(md_table, selected_column_index):

    md_table = md_table.replace('```', '')
    md_table = md_table.replace('**', '')

    lines = md_table.split('\n')

    lines = [lines[0]] + [line for line in lines[1:] if 'Derek' not in line]

    lines = lines[:1] + lines[2:]

    csv_lines = []
    student_table = []

    for line in lines:

        values = line.split('|')

        values = [v.strip() for v in values]

        if len(values) >= (selected_column_index + 1):

            first_column = values[1]
            second_column = values[2]

            selected_column_value = values[selected_column_index]

            csv_line = f"{first_column},{second_column},{selected_column_value}"

            csv_lines.append(csv_line)

            extracted_values = f"{first_column},{second_column},{selected_column_value}"

            student_table.append(extracted_values)

    csv_table = '\n'.join(csv_lines)

    return csv_table, student_table

def md_to_csv_file(md_file_path, csv_file_path, selected_column_index):
    """
    Convert a Markdown table from a file to a CSV file and save it.
    Additionally, extract a selected column from the Markdown table and save it as a separate CSV file.

    Args:
        md_file_path (str): The path to the Markdown file.
        csv_file_path (str): The path to save the converted CSV file.
        selected_column_index (int): The index of the column to extract and save as a separate CSV file.

    Returns:
        None
    """

    with open(md_file_path, 'r') as file:
        md_table = file.read()

    csv_table, student_table = md_to_csv(md_table, selected_column_index)

    # Write the CSV table to the output file
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

    print(Fore.YELLOW + f' 〉MD file loaded:   {md_file_path} ' + Style.RESET_ALL)
    print(Back.GREEN + Fore.WHITE + f' 〉CSV file saved:  {csv_file_path} ' + Style.RESET_ALL)
    print(Fore.YELLOW + f' 〉{output_file_name}\'s record saved:  {selected_file_path} ' + Style.RESET_ALL)
    print(Back.RED + Fore.YELLOW + f' 〉PDF file generated: {output_file_name}.pdf ' + Style.RESET_ALL)

# file paths
md_file_path = os.getenv('PATH_MD')
csv_file_path = os.getenv('PATH_PROGRESS_CSV')

selected_column_index = 4

for i in range(4, 21):
    selected_column_index = i
    current_csv_file_path_template = os.getenv('PATH_CSV_LOOP')
    current_csv_file_path = current_csv_file_path_template.replace('{i}', str(i))
    md_to_csv_file(md_file_path, current_csv_file_path, selected_column_index)

print('\n')
print(Fore.GREEN + ' 🏆 Done exporting all progress report CSVs for students ' + Style.RESET_ALL)
print('\n')



