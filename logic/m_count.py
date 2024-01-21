import os
import csv
import sys
import re
from colorama import Fore, Style, Back
from dotenv import load_dotenv
load_dotenv()

student_name = sys.argv[1]
csv_file_path_template = os.getenv('PATH_STUDENT_CSV')
csv_file_path = csv_file_path_template.replace('{student_name}', student_name)

def get_last_name(first_name):
    return os.getenv(f'{first_name.upper()}')

def extract_module_number(module_name):
    match = re.search(r'M(\d+)', module_name)

    return match.group(1) if match else None

def count_missing_exercises(csv_file_path):
    missing_counts = {}
    in_complete = 0
    locked = 0
    un_accepted = 0

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        full_name = get_last_name(f'{student_name}')
        print(Fore.WHITE + Back.CYAN + f" Student: {full_name} " + Style.RESET_ALL)

        for row in reader:
            module_name = row[0].rstrip('0123456789')
            module_no = extract_module_number(module_name)
            print(f'{module_no}')
            exercise_status = row[2] if len(row) > 2 else None
            print(f'status: {exercise_status}')

            if module_no is not None:
                if exercise_status != '✓':
                    missing_counts.setdefault(module_no, 0)
                    missing_counts[module_no] += 1
                if exercise_status == 'ic':
                    in_complete += 1
                elif exercise_status == 'L':
                    locked += 1
                elif exercise_status == 'U':
                    un_accepted += 1

        # Print the missing exercises per module
        for module, count in missing_counts.items():
            print(f"M{module}: {count} exercises missing")

        # Count modules without a checkmark (✓)
        for module_no in range(1, int(max(missing_counts.keys())) + 1):
            if module_no not in missing_counts:
                missing_counts[module_no] = 1


    return missing_counts, in_complete, locked, un_accepted

missing_counts, in_complete, locked, un_accepted = count_missing_exercises(csv_file_path)

print("----------------------------------")
print(Fore.WHITE + Back.LIGHTBLACK_EX + f" TOTALS:                        ⏚ " + Style.RESET_ALL)
print(f"MISSING exercises: {sum(missing_counts.values())}")
print(f"INCOMPLETE exercises: {in_complete}")
print(f"LOCKED exercises: {locked}")
print(f"UNACCEPTED exercises: {un_accepted}")
