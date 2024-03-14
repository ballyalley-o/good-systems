import csv
import os
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from logic.constants.constants import *
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

            print(f"Grades for {done}: {grades}")

            top_students = sorted(grades, key=grades.get, reverse=True)[:3]

            print(f"Top students for {done}: {top_students}")
            print('\n')

            # Add the top students for the current item to the top_students_all dictionary
            top_students_all[done] = top_students

            # Reset the CSV reader to the beginning of the file
            f.seek(0)
            next(reader)  # Skip the header

    return top_students_all



csv_file_path = os.getenv('PATH_ALL_CSV')
top_students = get_top_students(csv_file_path)
