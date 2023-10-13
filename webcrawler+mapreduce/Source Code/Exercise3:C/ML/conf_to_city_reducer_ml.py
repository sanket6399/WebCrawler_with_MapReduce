#!/usr/bin/env python3
import sys
import json

current_key = None
current_cities = []

# Specify the research area to filter (e.g., "Machine Learning")
desired_research_area = "ML"

for line in sys.stdin:
    # Split the input line by tab
    key, research_area, city = line.strip().split('\t')

    # Check if the research area matches the desired area
    if research_area == desired_research_area:
        # Combine conference acronym and research area as the key
        combined_key = f'{key}\t{research_area}'

        if current_key == combined_key:
            current_cities.append(city)
        else:
            if current_key:
                # Build a JSON object for the output
                output_data = {
                    "Conference_Acronym": current_key.split('\t')[0],
                    "Research_Area": current_key.split('\t')[1],
                    "Cities": current_cities
                }
                
                # Output the JSON object
                print(json.dumps(output_data))
            
            current_key = combined_key
            current_cities = [city]

# Output the last JSON object
if current_key:
    output_data = {
        "Conference_Acronym": current_key.split('\t')[0],
        "Research_Area": current_key.split('\t')[1],
        "Cities": current_cities
    }
    print(json.dumps(output_data))
