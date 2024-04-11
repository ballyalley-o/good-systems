#!/bin/bash

# Usage: ./grade.sh <student> <module> <exercise> <status>

csv_file="progress-all.csv"
temp_file="temp.csv"

student=$1

student_name=$(echo "$student" | awk '{print toupper(substr($0, 1, 1)) substr($0, 2)}')

if [ "$student_name" = "ALL" ]; then
    module=M$2
    exercise=$(echo "$3" | tr '[:lower:]' '[:upper:]')
    status=$4

    row=$(awk -v module="$module" -v exercise="$exercise" '$2 == module && $3 == exercise {print NR}' "$csv_file")

    awk -v row="$row" -v status="✓" -F, 'BEGIN {OFS = FS} NR == row {for (i=4; i<=NF; i++) $i = status} 1' "$csv_file" > "$temp_file" && mv "$temp_file" "$csv_file"

else

    column=$(head -1 "$csv_file" | tr ',' '\n' | grep -n -i "^$student_name$" | cut -d: -f1)

    if [ -z "$column" ]; then
        echo "Student not found"
        exit 1
    fi


    if [ "$2" = "mini" ]; then

        echo "Enter grade for Trainer 1 (0-10) : "
        read -p $'〉 ' grade1
        echo "Enter grade for Trainer 2 (0-10) : "
        read -p $'〉 ' grade2
        echo "Enter grade for Trainer 3 (0-10) : "
        read -p $'〉 ' grade3

        average=$(echo "scale=2; ($grade1 + $grade2 + $grade3) / 3" | bc -l)
        average_rounded=$(printf "%.2f\n" $(echo "$average + 0.005" | bc))
        status="$average_rounded"

        row=$(grep -n -i "^$3" "$csv_file" | cut -d: -f1)
        awk -v row="$row" -v column="$column" -v status="$status" -F, 'BEGIN {OFS = FS} NR == row {if(status=="done") $column="✓"; else if(status=="no") $column=""; else $column=status} 1' "$csv_file" > "$temp_file" && mv "$temp_file" "$csv_file"

        echo -n -e  "\n"
        echo -n -e " $student 〉 Mini-Project $3: Marked $status \n"
        echo -e "\n"

    fi

    module=M$2
    exercise=$(echo "$3" | tr '[:lower:]' '[:upper:]')
    status=$4

    row=$(grep -n -i "^$module - $exercise" "$csv_file" | cut -d: -f1 | head -n 1)
    awk -v row="$row" -v column="$column" -v status="$status" -F, 'BEGIN {OFS = FS} NR == row {if(status=="done") $column="✓"; else if(status=="no") $column=""; else $column=status} 1' "$csv_file" > "$temp_file" && mv "$temp_file" "$csv_file"
fi


