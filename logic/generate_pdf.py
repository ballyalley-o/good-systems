import csv
import os
from .constants.constants import *
from reportlab.lib.pagesizes import letter
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

    for row in data[1:]:
        first_name = data[0][2]
        full_name = get_last_name(first_name)

# --------------------------------------------------start build pdf--------------------------------------------------

    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    logo_path = os.getenv('PATH_LOGO')
    logo = Image(logo_path, width=130, height=45)

    name = f'{full_name}' if full_name else first_name
    gitu = data[1][2]

    data[1][0] = ''
    data[1][2] = ''
    data[0][2] = ''

    cohort = os.getenv('COHORT_NAME')
    cohort_name = os.getenv('COHORT_NAME')

    name_style = ParagraphStyle(
        'NameStyle',
        parent=getSampleStyleSheet()['Heading2'],
        spaceAfter=4,
    )

    gitu_style = ParagraphStyle(
        'GitUStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=1,
    )

    report_card_style = ParagraphStyle(
        'ReportCardStyle',
        parent=getSampleStyleSheet()['Heading4'],
        spaceBefore=2,
        spaceAfter=1,
        alignment=1,
        italics=1
    )

    cohort_name_style = ParagraphStyle(
        'CohortNameStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=1,
    )

    legend_file_path = os.getenv('PATH_LEGEND_CSV')

    with open(legend_file_path, 'r') as legend_file:
        reader = csv.reader(legend_file)
        legend_data = list(reader)

    legend = []
    for row in legend_data:
        legend.append(row)

    legend_style = ParagraphStyle(
        'LegendStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=1,
        fontSize=10
    )

    cutoff_style = ParagraphStyle(
        'CutOffStyle',
        parent=getSampleStyleSheet()['Normal'],
        spaceAfter=4,
        fontSize=8
    )

    doc.topMargin -= 20

    elements = [
        logo,
        Spacer(2, 6),
        Paragraph("Progress Report Card", report_card_style),
        Spacer(1, 6),
        Paragraph(name, name_style),
        Paragraph(gitu, gitu_style),
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

    elements.append(PageBreak())

    elements.append(legend_table)

    now = datetime.now()
    dt_string = now.strftime("%d %B %Y %H:%M:%S")
    elements.append(Spacer(1, 12))
    elements.append(Spacer(1, 12))
    elements.append(Spacer(1, 12))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(dt_string, legend_style))
    elements.append(Paragraph(CUTOFF_MESSAGE, cutoff_style))

    doc.build(elements)