import csv

def md_to_csv(md_table):
    md_table = md_table.replace('```', '')
    md_table = md_table.replace('**', '')

    lines = md_table.split('\n')
    lines = lines[:1] + lines[2:]

    csv_lines = []

    for line in lines:
        values = line.split('|')
        values = [v.strip() for v in values]
        csv_lines.append(values)

    return csv_lines

def md_to_csv_file(md_file_path, csv_file_path):
    with open(md_file_path, 'r') as file:
        md_table = file.read()

    csv_data = md_to_csv(md_table)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)

    print(f'Legend CSV file saved to {csv_file_path}')

# File paths
md_file_path = '/Users/bally/IOD/progress/legend.md'
csv_file_path = '/Users/bally/IOD/progress/csv/legend.csv'

md_to_csv_file(md_file_path, csv_file_path)
