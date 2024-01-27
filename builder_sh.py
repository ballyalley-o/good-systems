import os
import sys
from colorama import Fore, Style, Back
from logic.m_count import count_missing_exercises
from logic.calc_grade import calculate_grades
from dotenv import load_dotenv
load_dotenv()

student_name = sys.argv[1]
csv_file_path_template = os.getenv('PATH_STUDENT_CSV')
csv_file_path = csv_file_path_template.replace('{student_name}', student_name)

print('\n')
missing_counts, in_complete, locked, un_accepted, in_progress = count_missing_exercises(csv_file_path)

if sum(missing_counts.values()) == 0 and sum(in_complete.values()) == 0 and sum(locked.values()) == 0 and sum(un_accepted.values()) == 0 and sum(in_progress.values()) == 0:
    print('\n')
    print(Fore.WHITE + Back.LIGHTBLACK_EX + ' 🥇  No missing exercises ' + Style.RESET_ALL)

    print('\n')
else:
    print('\n')
    print(Fore.WHITE + Back.LIGHTBLACK_EX + f" TOTALS:                        ⏚ " + Style.RESET_ALL)
    print(Fore.RED + f" MISSING: {sum(missing_counts.values())} " +  Style.RESET_ALL)
    print(Fore.MAGENTA + f" INPROGRESS: {sum(in_progress.values())} " +  Style.RESET_ALL)
    print(Fore.YELLOW + f" INCOMPLETE: {sum(in_complete.values())} " +  Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + f" LOCKED: {sum(locked.values())} " +  Style.RESET_ALL)
    print(Fore.LIGHTWHITE_EX + f" UNACCEPTED: {sum(un_accepted.values())} " + Style.RESET_ALL)
    print('\n')
    print(Fore.BLACK + Back.LIGHTCYAN_EX + f" Grades:                        ⏚ " + Style.RESET_ALL)
    # print(Fore.BLUE + f" {grades}" +  Style.RESET_ALL)
    calculate_grades(csv_file_path)