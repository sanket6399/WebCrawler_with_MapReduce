#!/usr/bin/env python3
import sys

# Specify the research area to filter (e.g., "Machine Learning")
desired_research_area = "AI"

for line in sys.stdin:
    # Split the input line by tab
    columns = line.strip().split('\t')
    
    if len(columns) >= 6:
        acronym = columns[0]
        research_area = columns[5]
        city = columns[3]
        
        # Check if the research area matches the desired area
        if research_area == desired_research_area:
            # Emit key-value pair (conference_acronym, research_area) as key
            # and city as the value
            print(f'{acronym}\t{research_area}\t{city}')
