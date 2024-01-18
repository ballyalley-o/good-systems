import os

def md_to_csv(md_table, selected_column_index):
    md_table = md_table.replace('```', '')
    md_table = md_table.replace('**', '')

    lines = md_table.split('\n')

    exclude = os.getenv('EXCLUDE')

    lines = [lines[0]] + [line for line in lines[1:] if exclude not in line]

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