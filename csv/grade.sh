#!/bin/bash

# Usage: ./update_grade.sh <student> <module> <exercise> <status>

csv_file="dummy.csv"
temp_file="temp.csv"

student=$1
module=$2
exercise=$3
status=$4

student_name=$(echo "$student" | awk '{print toupper(substr($0, 1, 1)) substr($0, 2)}')

if [ "$student_name" = "ALL" ]; then

    row=$(awk -v module="$module" -v exercise="$exercise" '$2 == module && $3 == exercise {print NR}' "$csv_file")

    awk -v row="$row" -v status="✓" -F, 'BEGIN {OFS = FS} NR == row {for (i=4; i<=NF; i++) $i = status} 1' "$csv_file" > "$temp_file" && mv "$temp_file" "$csv_file"
else

    column=$(head -1 "$csv_file" | tr ',' '\n' | grep -n -i "^$student_name$" | cut -d: -f1)

    row=$(grep -n -i "^$module - $exercise" "$csv_file" | cut -d: -f1)

    awk -v row="$row" -v column="$column" -v status="$status" -F, 'BEGIN {OFS = FS} NR == row {if(status=="done") $column="✓"; else $column=status} 1' "$csv_file" > "$temp_file" && mv "$temp_file" "$csv_file"
fi
