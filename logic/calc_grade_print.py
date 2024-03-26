import os
import csv
import re
from colorama import Fore, Back, Style
from dotenv import load_dotenv
load_dotenv()


def extract_module_number(module_name):
    if module_name.startswith("MX"):
        match = re.search(r'M([A-Za-z])', module_name)
        return match.group(1) if match else None
    else:
        match = re.search(r'M(\d+)', module_name)
        return match.group(1) if match else None


def calculate_grades_print(csv_file_path):
    def get_last_name(first_name):
        return os.getenv(f'{first_name.upper()}')

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        total_exercises = {}
        completed_exercises = {}

        for row in reader:
            module_name = row[0].rstrip('0123456789')
            module_no = extract_module_number(module_name)
            exercise_status = row[2] if len(row) > 2 else None

            if module_no is not None:
                total_exercises.setdefault(module_no, 0)
                total_exercises[module_no] += 1

                if exercise_status == '✓':
                    completed_exercises.setdefault(module_no, 0)
                    completed_exercises[module_no] += 1

        grades = {}
        for module_no in total_exercises.keys():
            total = total_exercises[module_no]
            completed = completed_exercises.get(module_no, 0)
            grades[module_no] = 10 / total * completed


        return grades


