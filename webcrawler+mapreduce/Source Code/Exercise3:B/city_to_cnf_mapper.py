#!/usr/bin/env python3
import sys
import json
''' Storing the output in json format, key will be City and then as per each city,  count will be increased in reducer'''

for line in sys.stdin:
    items = line.strip().split('\t')        # taking the input of each line

    if len(items) >= 3:
        city_data = items[3].strip()        # data cleaning by removing leading and trailing spaces if there are any
        city_data = city_data.lstrip()
        if city_data:
            city = city_data.strip()
            count = 1
            conference_names = [items[2]]  # the conference name is in items[0]
            city_data = {
                "City": city,
                "Count": count,
                "Conferences": conference_names
            }
            print(json.dumps(city_data))
