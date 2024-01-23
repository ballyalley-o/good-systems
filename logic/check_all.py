from .constants.constants import *

def check_rows(data):
    for count, row in enumerate(data):
        if row[0].startswith(('M', 'C', '1', '2', '3', '0', '★')) and row[0] != MODULE:

            if not row[2]:
                return False

            elif any(x in row[2] for x in EXERCISE_STATUS):
                return False

    return True
