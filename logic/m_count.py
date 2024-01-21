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
    in_complete = {}
    locked = {}
    un_accepted = {}

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        full_name = get_last_name(f'{student_name}')
        print(Fore.WHITE + Back.CYAN + f" Student: {full_name} " + Style.RESET_ALL)
        print('\n')

        for row in reader:
                module_name = row[0].rstrip('0123456789')
                module_no = extract_module_number(module_name)
                exercise_status = row[2] if len(row) > 2 else None

                if module_no is not None:
                    if exercise_status != '✓' and exercise_status != 'ic' and exercise_status != 'L' and exercise_status != 'U':
                        missing_counts.setdefault(module_no, 0)
                        missing_counts[module_no] += 1
                    if exercise_status == 'ic':
                        in_complete.setdefault(module_no, 0)
                        in_complete[module_no] += 1
                        # in_complete += 1
                    elif exercise_status == 'L':
                        locked.setdefault(module_no, 0)
                        locked[module_no] += 1
                    elif exercise_status == 'U':
                        un_accepted.setdefault(module_no, 0)
                        un_accepted[module_no] += 1

        for module, count in missing_counts.items():
            print(Fore.RED + f"{module}, MISSING: {count}" + Style.RESET_ALL)

        for module, count in in_complete.items():
            print(Fore.YELLOW + f"{module}, INCOMPLETE: {count}" + Style.RESET_ALL)

        for module, count in locked.items():
            print(Fore.LIGHTBLACK_EX + f"{module}, LOCKED: {count}" + Style.RESET_ALL)

        for module, count in un_accepted.items():
            print(Fore.LIGHTWHITE_EX + f"{module}, UNACCEPTED: {count}" + Style.RESET_ALL)

    return missing_counts, in_complete, locked, un_accepted

missing_counts, in_complete, locked, un_accepted = count_missing_exercises(csv_file_path)

print("----------------------------------")
print(Fore.WHITE + Back.LIGHTBLACK_EX + f" TOTALS:                        ⏚ " + Style.RESET_ALL)
print('\n')
print(Fore.RED + f" MISSING: {sum(missing_counts.values())} " +  Style.RESET_ALL)
print(Fore.YELLOW + f" INCOMPLETE: {sum(in_complete.values())} " +  Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + f" LOCKED: {sum(locked.values())} " +  Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX + f" UNACCEPTED: {sum(un_accepted.values())} " + Style.RESET_ALL)
print('\n')
