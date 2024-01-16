import csv

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

            # Join the values into a CSV-formatted line
            csv_line = f"{first_column},{second_column},{selected_column_value}"

            # Add the line to the CSV lines list
            csv_lines.append(csv_line)

            extracted_values = f"{first_column},{second_column},{selected_column_value}"

            student_table.append(extracted_values)

    csv_table = '\n'.join(csv_lines)

    return csv_table, student_table

def md_to_csv_file(md_file_path, csv_file_path, selected_column_index):

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

    selected_file_path = f'/Users/bally/IOD/progress/students/{output_file_name}.csv'

    with open(selected_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Split student_table_str into rows
        rows = [row.split(',') for row in student_table_str.split('\n')]
        writer.writerows(rows)

    print(f'CSV file saved to {csv_file_path}!')
    print(f'{output_file_name}\'s record saved to {selected_file_path}!')

# file paths
md_file_path = '/Users/bally/IOD/progress/progress.md'
csv_file_path = '/Users/bally/IOD/progress/students/progress.csv'


selected_column_index = 4

md_to_csv_file(md_file_path, csv_file_path, selected_column_index)

# TODO:after generating the csv, put the table in a pdf file


