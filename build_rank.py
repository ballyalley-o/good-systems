import csv
import os
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from logic.constants.constants import *
from itertools import groupby
from dotenv import load_dotenv
load_dotenv()

def get_top_students(csv_file_path):
    """
    Get the top 3 students based on their grades in the mini-project.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        list: The top 3 students.

    """
    top_students_all = {}

    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        students = header[2:]


        for done in DONE:
            grades = {}
            for row in reader:
                if row[1] == MINI_PROJECT and row[0] == done:
                    for i, grade in enumerate(row[2:], start=2):
                        grades[students[i - 2]] = grade

            # print(f"Grades for {done}: {grades}")

            sorted_students = sorted(grades.items(), key=lambda x: x[1], reverse=True)

            top_groups = []
            current_group = [sorted_students[0]]

            for student, grade in sorted_students[1:]:
                if grade == current_group[0][1]:
                    current_group.append((student, grade))
                else:
                    top_groups.append(current_group)
                    current_group = [(student, grade)]

                if len(top_groups) == 3:
                    break

            if len(top_groups) < 3 and current_group:
                top_groups.append(current_group)

            top_students = [group for group in top_groups]

            tied_students = [group for group in top_students if len(group) > 1]

            print(f"Top students for {done}: {top_students}")
            print('\n')

            top_students_all[done] = top_students

            f.seek(0)
            next(reader)

        return top_students_all


csv_file_path = os.getenv('PATH_ALL_CSV')
top_students = get_top_students(csv_file_path)
