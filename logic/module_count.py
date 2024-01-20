import os
import csv
import io
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

md_file_path = os.getenv('PATH_MD')
csv_file_path = os.getenv('PATH_STUDENT_CSV')

with open(md_file_path, 'r') as file:
    md_table = file.read()

# Convert MD table to DataFrame
df = pd.read_csv(io.StringIO(md_table), delimiter=',')  # Change '|' to ','

# Write DataFrame to CSV file
df.to_csv(csv_file_path, index=False)

# Print the converted CSV file
print(f"CSV file: {csv_file_path}")

# Read the CSV file into a list of lists
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    list2 = list(reader)
    # print(f"rows: {list2}")

def count_exercises_per_module(data):
    exercise_count_per_module = {}
    unsubmitted_exercises = {}

    for row in data[1:]:
        module_name = row[0].rstrip('0123456789')
        exercise_status = row[2]

        if 'M' not in module_name:
            module_name = 'Pre-work'

        if module_name not in exercise_count_per_module:
            exercise_count_per_module[module_name] = 0

        if exercise_status != '✓':
            missing_exercises = [f"Exercise {index + 1}" for index, status in enumerate(row[3:], start=1) if status != '✓']
            unsubmitted_exercises.setdefault(module_name, []).extend(missing_exercises)
            exercise_count_per_module[module_name] += 1

    print(f"unsubmitted_exercises before processing: {unsubmitted_exercises}")

    return exercise_count_per_module, unsubmitted_exercises

