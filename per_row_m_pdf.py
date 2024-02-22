import os
import csv
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from logic.constants.constants import *
from logic.styles.table import *
from dotenv import load_dotenv
load_dotenv()

def get_incomplete_students(csv_file_path, module):
    module = module.upper()
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        students = header[2:]
        incomplete_students = {}

        for row in reader:
            if row[0].startswith(module):
                exercise = row[0]
                incomplete_students[exercise] = []
                for i, status in enumerate(row[2:], start=2):
                    if status != '✓':
                        incomplete_students[exercise].append(students[i - 2])

        return incomplete_students

def generate_pdf_report(incomplete_students, module):
    doc = SimpleDocTemplate(f"pdf/{module}_report.pdf", pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    header = Paragraph(f"{MISSING_EXERCISES_MSG_PDF}", styles['Heading1'])  # Fix: Added closing parentheses and defined "f" string prefix
    elements.append(header)

    for exercise, students in incomplete_students.items():
        if students:
            data = [[f"{exercise}:"]]
            data.extend([[student] for student in students])
            table = Table(data, colWidths=460)
            table.setStyle(TableStyle(styles_table_missing(data)))
            elements.append(table)

    doc.build(elements)

csv_file_path =  os.getenv('PATH_ALL_CSV')
module = sys.argv[1]
incomplete_students = get_incomplete_students(csv_file_path, module)
generate_pdf_report(incomplete_students, module)



