import csv
import os
from .constants.constants import *
from .styles.table import *
from .check_all import check_rows
from .style_missing import *
from .calc_grade_print import calculate_grades_print
from .m_count import extract_module_number
from build_rank import get_top_students
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Image
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def get_last_name(first_name):
    return os.getenv(f'{first_name.upper()}')

def generate_pdf(md_csv_pdf_file, csv_file_path, output_file_name):
    """
    Generate a PDF file based on the provided CSV file.

    Args:
        csv_file_path (str): The path to the CSV file.
        output_file_name (str): The name of the output PDF file.

    Returns:
        None
    """
    pdf_file_path_template = os.getenv('PATH_PDF')
    pdf_file_path = pdf_file_path_template.replace('{output_file_name}', output_file_name)

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    legend_file_path = os.getenv('PATH_LEGEND_CSV')
    with open(legend_file_path, 'r') as legend_file:
        reader = csv.reader(legend_file)
        legend_data = list(reader)

    first_name = data[0][2]
    full_name = get_last_name(first_name)
    gitu = data[1][2]

    data[1][0] = ''
    data[1][2] = ''
    data[0][2] = ''

    all_exercises_done = check_rows(data)

    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    logo_path = os.getenv('PATH_LOGO')
    logo = Image(logo_path, width=130, height=45)

    name = f'{full_name}' if full_name else first_name
    cohort_name = os.getenv('COHORT_NAME')

    name_style = ParagraphStyle('NameStyle', parent=getSampleStyleSheet()['Heading2'], spaceAfter=4)
    gitu_style = ParagraphStyle('GitUStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=1)
    report_card_style = ParagraphStyle('ReportCardStyle', parent=getSampleStyleSheet()['Heading4'], spaceBefore=2, spaceAfter=1, alignment=1, italics=1)
    cohort_name_style = ParagraphStyle('CohortNameStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=1)
    cutoff_style = ParagraphStyle('CutOffStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=4, fontSize=8)
    date_style = ParagraphStyle('DateStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=12, fontSize=10)

    now = datetime.now()
    dt_string = now.strftime("%d %B %Y %H:%M:%S")

    csv_path = os.getenv('PATH_ALL_CSV')
    top_students = get_top_students(csv_path)

    if first_name in top_students:
        mp1 = f'{MP1_RANK.format(top_students.index(first_name) + 1)}'
        # mp1 = f'Mini-Project 1 | ★ TOP {top_students.index(first_name) + 1}'
        if first_name == top_students[0]:
            text_color=colors.gold
        elif first_name == top_students[1]:
            text_color=colors.silver
        else :
            text_color=colors.brown


        mp1_style = ParagraphStyle('NameStyle', parent=getSampleStyleSheet()['Heading4'], spaceAfter=1, textColor=text_color)

    elements = [
        logo,
        Spacer(2, 6),
        Paragraph(REPORT_CARD_TITLE, report_card_style),
        Spacer(1, 6),
        Paragraph(name, name_style),
        Paragraph(gitu, gitu_style),
        Spacer(1, 4),
        Paragraph(cohort_name, cohort_name_style),
        Spacer(1, 12),
        Paragraph(mp1, mp1_style),
    ]

    # grade implementation
    grades = calculate_grades_print(csv_file_path)

    i = 0
    while i < len(data):
        row = data[i]
        module_name = row[0].rstrip('0123456789')
        module_no = extract_module_number(module_name)
        grade = grades.get(module_no)


        if row[0] == 'MX' and i > 0 and isinstance(data[i - 1][1], str) and data[i - 1][1].startswith('GRADE:'):
            data.pop(i - 1)

        if (i == len(data) - 1 or (i + 1 < len(data) and extract_module_number(data[i + 1][0]) != module_no)):
            if grade is not None:
                grade_row = ['', f'GRADE: {grade:.2f}', '']
                data.insert(i + 1, grade_row)

        i += 1

    table = Table(data)
    styles_table = styles_table_main(data)
    table.setStyle(TableStyle(styles_table))
    legend_table = Table(legend_data)
    styles = style_missing(data)
    table.setStyle(TableStyle(styles))
    styles_legend = style_missing_legend(legend_data)
    legend_table.setStyle(TableStyle(styles_legend, repeatRows=1))

    if all_exercises_done:
        header = [EXERCISES_COMPLETED]
        completed_table = Table([header])
        styles_completed = styles_table_completed(data)
        completed_table.setStyle(TableStyle(styles_completed))
        elements.append(completed_table)

    elements.extend([
        Spacer(1, 12),
        table,
        Spacer(1, 12),
        Spacer(1, 12),
        Spacer(1, 12),
        PageBreak(),
        legend_table,
        Spacer(1, 12),
        Spacer(1, 12),
        Spacer(1, 12),
        Spacer(1, 12),
        Paragraph(dt_string, date_style),
        Paragraph(CUTOFF_MESSAGE, cutoff_style)
    ])

    doc.build(elements)