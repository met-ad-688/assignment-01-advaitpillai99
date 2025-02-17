#!/bin/bash

# Count occurrences of "python" in the extracted CSV files
count=$(grep -i "python" question_tags.csv questions.csv | wc -l)

echo "Number of lines containing 'python': $count"


