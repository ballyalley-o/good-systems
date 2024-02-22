import os
import csv
import sys
from colorama import Fore, Style
from logic.constants.constants import *
from dotenv import load_dotenv
load_dotenv()

def get_incomplete_students(csv_file_path, module, exercise):
    module_exercise = f'{module.upper()} - {exercise.upper()}'
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        students = header[2:]
        incomplete_students = []

        for row in reader:
            if row[0] == module_exercise:
                for i, status in enumerate(row[2:], start=2):
                    if status != '✓':
                        incomplete_students.append(students[i - 2])

        return incomplete_students

csv_file_path =  os.getenv('PATH_ALL_CSV')
module = sys.argv[1]
exercise = sys.argv[2]
incomplete_students = get_incomplete_students(csv_file_path, module, exercise)

print('\n')
print(Fore.RED + MISSING_EXERCISES_MSG.format(f'{module.upper()}', f'{exercise.upper()}') + Style.RESET_ALL)
print('\n')
for student in incomplete_students:
    print(student)
print('\n')
