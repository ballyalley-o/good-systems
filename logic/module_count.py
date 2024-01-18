def count_exercises_per_module(data):
    exercise_count_per_module = {}
    unsubmitted_exercises = {}

    for row in data[1:]:
        module_name = row[0].rstrip('0123456789')
        exercise_status = row[2]

        if 'M' not in module_name:
            module_name = 'Pre-work'

        if exercise_status == '✓':
            if module_name not in exercise_count_per_module:
                exercise_count_per_module[module_name] = 1
            else:
                exercise_count_per_module[module_name] += 1
        else:
            if module_name not in exercise_count_per_module:
                exercise_count_per_module[module_name] = 0

            if module_name not in unsubmitted_exercises:
                unsubmitted_exercises[module_name] = [f"Exercise {index + 1}" for index, status in enumerate(row[3:], start=1) if status != '✓']
            else:
                unsubmitted_exercises[module_name].extend([f"Exercise {index + 1}" for index, status in enumerate(row[3:], start=1) if status != '✓'])

    return exercise_count_per_module, unsubmitted_exercises