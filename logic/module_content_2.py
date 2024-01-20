import os
import csv
import sys
# from generate_pdf import get_last_name
from dotenv import load_dotenv
load_dotenv()

student_name = sys.argv[1]
csv_file_path_template = os.getenv('PATH_STUDENT_CSV')
csv_file_path = csv_file_path_template.replace('{student_name}', student_name)

def get_last_name(first_name):

    return os.getenv(f'{first_name.upper()}')

def count_missing_exercises(csv_file_path):
    missing_count = 0
    in_complete = 0
    locked = 0
    un_accepted = 0

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        full_name = get_last_name(f'{student_name}')
        # full_name = full_name_template.replace('{student_name}', student_name)
        print(f"Student: {full_name}")

        for row in reader:
            module_prework = row[0]
            module_name = row[0].rstrip('0123456789')
            module_no = module_name.rstrip(' - E - P - E7 Part')
            exercise_status = row[2] if len(row) > 2 else None

            module_name

            if module_name.startswith('M') and exercise_status != '✓':
                missing_count += 1
                # if module_no is the same number as the previous module_no, then add collect them together
                print(f"{module_no}, MISSING: {missing_count}")
                # print(f"{module_no}, MISSING: {missing_count}")
            if module_name.startswith('M') and exercise_status == 'ic':
                in_complete += 1
                print(f"{module_no}, INCOMPLETE: {in_complete}")
            if module_name.startswith('M') and exercise_status == 'L':
                locked += 1
                print(f"{module_no}, LOCKED: {locked}")
            if module_name.startswith('M') and exercise_status == 'U':
                un_accepted += 1
                print(f"{module_no}, UNACCEPTED: {un_accepted}")

    return missing_count, in_complete, locked, un_accepted

missing_count, in_complete, locked, un_accepted = count_missing_exercises(csv_file_path)
print(f"Number of MISSING exercises: {missing_count}")
print(f"Number of INCOMPLETE exercises: {in_complete}")
print(f"Number of LOCKED exercises: {locked}")
print(f"Number of UNACCEPTED exercises: {un_accepted}")

