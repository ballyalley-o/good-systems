import csv
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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
    with open(md_file_path, 'r') as file:
        md_table = file.read()

    csv_table, student_table = md_to_csv(md_table, selected_column_index)

    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        rows = [row.split(',') for row in csv_table.split('\n')]
        writer.writerows(rows)

    student_table_str = '\n'.join(student_table)

    output_file_name = rows[0][2]

    selected_file_path = f'/Users/bally/IOD/progress/students/{output_file_name}.csv'

    with open(selected_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        rows = [row.split(',') for row in student_table_str.split('\n')]
        writer.writerows(rows)

    generate_pdf(selected_file_path, output_file_name)

    print(f'CSV file saved to {csv_file_path}')
    print(f'{output_file_name}\'s record saved to {selected_file_path}')
    print(f'PDF file generated: {output_file_name}.pdf')

def get_last_name(first_name):

    return os.getenv(f'{first_name.upper()}')

def generate_pdf(csv_file_path, output_file_name):
    pdf_file_path = f'/Users/bally/IOD/progress/pdf/{output_file_name}.pdf'

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    for row in data[1:]:
        first_name = data[0][2]
        full_name = get_last_name(first_name)


    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    logo_path = '/Users/bally/IOD/progress/assets/iod.png'
    logo = Image(logo_path, width=150, height=52)


    name = f'{full_name}' if full_name else first_name
    gitu = data[1][2]

    data[1][0] = ''
    data[1][2] = ''
    data[0][2] = ''




    cohort_name = os.getenv('COHORT_NAME')

    name_style = ParagraphStyle(
        'NameStyle',
        parent=getSampleStyleSheet()['Heading1'],
        spaceAfter=1,
    )

    gitu_style = ParagraphStyle(
        'GitUStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=1,
    )

    report_card_style = ParagraphStyle(
        'ReportCardStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceBefore=2,
        spaceAfter=2,
    )

    cohort_name_style = ParagraphStyle(
        'CohortNameStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceBefore=2,
    )

    # add the legend.csv file to the pdf
    legend_file_path = '/Users/bally/IOD/progress/csv/legend.csv'

    with open(legend_file_path, 'r') as legend_file:
        reader = csv.reader(legend_file)
        legend_data = list(reader)

    # add the legend to the pdf
    legend = []
    for row in legend_data:
        legend.append(row)

    legend_style = ParagraphStyle(
        'LegendStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=1,
    )

    elements = [
        logo,
        Spacer(2, 6),
        Paragraph(name, name_style),
        Paragraph(gitu, gitu_style),
        Spacer(1, 6),
        Paragraph("Progress Report Card", report_card_style),
        Spacer(1, 4),
        Paragraph(cohort_name, cohort_name_style),
        Spacer(1, 12),
    ]

    table = Table(data)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), 'black'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
    ]))

    legend_table = Table(legend)
    legend_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), 'black'),
        ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))
    elements.append(Spacer(1, 12))
    elements.append(Spacer(1, 12))

    elements.append(legend_table)

    doc.build(elements)

# file paths
md_file_path = '/Users/bally/IOD/progress/progress.md'
csv_file_path = '/Users/bally/IOD/progress/students/progress.csv'

selected_column_index = 5

for i in range(4, 21):
    selected_column_index = i
    current_csv_file_path = f'/Users/bally/IOD/progress/students/progress_{i}.csv'
    md_to_csv_file(md_file_path, current_csv_file_path, selected_column_index)



