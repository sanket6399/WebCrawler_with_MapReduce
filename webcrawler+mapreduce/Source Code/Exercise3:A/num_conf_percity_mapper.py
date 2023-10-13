#!/usr/bin/env python3
import sys

for line in sys.stdin:
    input_line = line.strip().split('\t')           #as our input file is in tsv format

    if len(input_line) >= 3:
        location = input_line[3].strip()           #taking raw city input
        location = location.lstrip()          #removing leading spaces if any left after data cleaning
        #city_data = location.split(',')

        if city_data:
            city = city_data[0].strip()
            print(f"{city}\t1")                 #storing in intermediate space
