import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from logic.constants.constants import *

def get_top_students(csv_file_path):
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        students = header[2:]
        grades = {}

        for row in reader:
            # print(f"Row: {row}")  # Debug print
            if row[1] == MINI_PROJECT and row[0] == '1':
                for i, grade in enumerate(row[2:], start=2):
                    grades[students[i - 2]] = grade

            # if row[1] == 'MINI-PROJECT' and row[0] == '2' and row[2:] == [''] * len(students):
            #     pass
            # else:
            #     for i, grade in enumerate(row[3:], start=3):
            #         grades[students[i - 2]] = grade


        print(f"Grades: {grades}")

        top_students = sorted(grades, key=grades.get, reverse=True)[:3]

        print(f"Top students: {sorted(grades, key=grades.get, reverse=True)[:3]}")
        print('\n')

        return top_students

