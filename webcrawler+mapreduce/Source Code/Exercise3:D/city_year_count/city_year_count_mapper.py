#!/usr/bin/env python3
import sys

# Process each line from standard input
for line in sys.stdin:
    # splitting the input line to make a tuple below
    input_line = line.strip().split('\t')
    if len(input_line) >= 3:
        location = input_line[3].strip()		#taking raw city input
        year =  input_line[1].strip()         #taking raw year input
    # intermediate space printing for reducer
    print(f"{location} {year}\t1")

