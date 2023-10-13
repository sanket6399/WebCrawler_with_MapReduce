#!/usr/bin/env python3
import sys
import json

current_city = None
city_data = {}      #json to store the output

for l in sys.stdin:
    data = json.loads(l.strip())     #as our mapper was putting data into json chunks, we pick it up using json.load
    location = data["City"]
    city = location.lstrip().strip()        #removing leading and trailing spaces to normalise the data
    
    if current_city == city:            #increment the data count and put if the city is same and conferences are different, append it
        city_data["Count"] += data["Count"]
        city_data["Conferences"].extend(data["Conferences"])
    else:
        if current_city:
            print(json.dumps(city_data))
        current_city = city
        city_data = {
            "City": city,
            "Count": data["Count"],
            "Conferences": data["Conferences"]      #final json will be a three level json data, with city having multiple conferences and its number
        }

if current_city:
    print(json.dumps(city_data))
