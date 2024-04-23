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

bronze = colors.Color(0.8, 0.5, 0.2)

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
    cutoff_header_style = ParagraphStyle('CutOffStyle', parent=getSampleStyleSheet()['Heading5'], spaceAfter=4, fontSize=8)
    cutoff_style = ParagraphStyle('CutOffStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=4, fontSize=8)
    cutoff_sub_style = ParagraphStyle('CutOffStyle', parent=getSampleStyleSheet()['Heading5'], spaceAfter=4, fontSize=6)
    date_style = ParagraphStyle('DateStyle', parent=getSampleStyleSheet()['Normal'], spaceAfter=12, fontSize=10)

    now = datetime.now()
    dt_string = now.strftime("%d %B %Y %H:%M:%S")

    csv_path = os.getenv('PATH_ALL_CSV')
    top_students_all = get_top_students(csv_path)

    def calculate_rank_and_color(first_name, top_students, rank_format, each_mp):
        text_color = colors.black
        mp = ''

        for rank, group in enumerate(top_students, start=1):
            if first_name in [student for student, _ in group]:
                mp = rank_format.format(each_mp, rank)
                if rank == 1:
                    text_color = colors.gold
                elif rank == 2:
                    text_color = colors.silver
                else:
                    text_color = bronze
                break

        return mp, text_color

    top_students_all = get_top_students(csv_path)

    mps = []
    styles = []

    for mp in DONE:
        mp_rank, text_color = calculate_rank_and_color(first_name, top_students_all[mp], MP_RANK, mp)
        mp_style = ParagraphStyle('NameStyle', parent=getSampleStyleSheet()['Heading4'], textColor=text_color)
        mps.append(mp_rank)
        styles.append(mp_style)

    elements = [
        logo,
        Spacer(2, 6),
        Paragraph(REPORT_CARD_TITLE, report_card_style),
        Spacer(1, 6),
        Paragraph(name, name_style),
        Paragraph(gitu, gitu_style),
        Spacer(1, 4),
        Paragraph(cohort_name, cohort_name_style),
        Spacer(1, 6),
    ]
    for mp, style in zip(mps, styles):
        elements.append(Paragraph(mp, style))

    grades = calculate_grades_print(csv_file_path)

    i = 0
    while i < len(data):
        row = data[i]
        module_name = row[0].rstrip('0123456789')
        module_no = extract_module_number(module_name)
        grade = grades.get(module_no)

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

    # final awards
    # TODO: automate this

    if first_name == os.getenv('EXCELLENCE_AWARD'):
        header = [EXCELLENCE_AWARDEE]
        excellence_table = Table([header])
        styles_excellence = styles_table_excellence(data)
        excellence_table.setStyle(TableStyle(styles_excellence))
        elements.append(excellence_table)

    if first_name == os.getenv('CONSISTENCY_AWARD'):
        header = [CONSISTENCY_AWARDEE]
        consistency_table = Table([header])
        styles_consistency = styles_table_consistency(data)
        consistency_table.setStyle(TableStyle(styles_consistency))
        elements.append(consistency_table)

    if first_name == os.getenv('ENGAGEMENT_AWARD'):
        header = [ENGAGEMENT_AWARDEE]
        engagement_table = Table([header])
        styles_engagement = styles_table_engagement(data)
        engagement_table.setStyle(TableStyle(styles_engagement))
        elements.append(engagement_table)

    if first_name == os.getenv('SYNERGY_MAESTRO_AWARD'):
        header = [SYNERGY_MAESTRO_AWARDEE]
        synergy_maestro_table = Table([header])
        styles_synergy_maestro = styles_table_team_player(data)
        synergy_maestro_table.setStyle(TableStyle(styles_synergy_maestro))
        elements.append(synergy_maestro_table)

    if first_name in os.getenv('TOP_CAPSTONE'):
        header = [TOP_CAPSTONE]
        top_capstone_table = Table([header])
        styles_top_capstone = styles_table_capstone(data)
        top_capstone_table.setStyle(TableStyle(styles_top_capstone))
        elements.append(top_capstone_table)

    if all_exercises_done:
        header = [EXERCISES_COMPLETED]
        completed_table = Table([header])
        styles_completed = styles_table_completed(data)
        completed_table.setStyle(TableStyle(styles_completed))
        elements.append(completed_table)


    ex_runner_ups = os.getenv('EXCELLENCE_AWARD_RUNNER_UP')
    runner_up_list = ex_runner_ups.split(";")

    co_runner_ups = os.getenv('CONSISTENCY_AWARD_RUNNER_UP')
    co_runner_up_list = co_runner_ups.split(";")

    en_runner_ups = os.getenv('ENGAGEMENT_AWARD_RUNNER_UP')
    en_runner_up_list = en_runner_ups.split(";")

    sm_runner_ups = os.getenv('SYNERGY_MAESTRO_RUNNER_UP')
    sm_runner_up_list = sm_runner_ups.split(";")

    tc_runner_ups = os.getenv('TOP_CAPSTONE')
    tc_runner_up_list = tc_runner_ups.split(";")



    elements.extend([
        Spacer(1, 6),
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
        Paragraph(CUTOFF_MESSAGE, cutoff_style),
        Spacer(1, 12),

        Paragraph(CUTOFF_HEADER_1, cutoff_header_style),
        Paragraph(CUTOFF_MESSAGE_1, cutoff_style),
        Paragraph(CUTOFF_MESSAGE_1_1.format(runner_up_list[0], runner_up_list[1], runner_up_list[2]), cutoff_sub_style),

        Paragraph(CUTOFF_HEADER_2, cutoff_header_style),
        Paragraph(CUTOFF_MESSAGE_2, cutoff_style),
        Paragraph(CUTOFF_MESSAGE_2_1.format(co_runner_up_list[0], co_runner_up_list[1], co_runner_up_list[2]), cutoff_sub_style),

        Paragraph(CUTOFF_HEADER_3, cutoff_header_style),
        Paragraph(CUTOFF_MESSAGE_3, cutoff_style),
        Paragraph(CUTOFF_MESSAGE_3_1.format(en_runner_up_list[0], en_runner_up_list[1], en_runner_up_list[2]), cutoff_sub_style),

        Paragraph(CUTOFF_HEADER_4, cutoff_header_style),
        Paragraph(CUTOFF_MESSAGE_4, cutoff_style),
        Paragraph(CUTOFF_MESSAGE_4_1.format(sm_runner_up_list[0], sm_runner_up_list[1]), cutoff_sub_style),

        Paragraph(CUTOFF_HEADER_5, cutoff_header_style),
        Paragraph(CUTOFF_MESSAGE_5_1.format(tc_runner_up_list[0], tc_runner_up_list[1], tc_runner_up_list[2]), cutoff_sub_style),

        Spacer(1, 12),
        Spacer(1, 12),
        Paragraph(CUTOFF_MESSAGE_0, cutoff_style),
    ])

    doc.build(elements)