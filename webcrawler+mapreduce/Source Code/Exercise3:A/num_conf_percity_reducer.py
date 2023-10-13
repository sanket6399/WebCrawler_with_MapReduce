#!/usr/bin/env python3
import sys

curr_city = None     #initialising the variables
curr_cnt = 0

for line in sys.stdin:
    city, count = line.strip().split('\t')
    count = int(count)
    # cleaning data by removing leading and trainling spaces
    city = city.lstrip().strip()

    if curr_city == city:        #if we have the same city, we increment the counter
        curr_cnt += count
    else:
        if curr_city:
            print(f"{curr_city}\t{curr_cnt}")       #if new city, just add the entry similar to wordcount program
        curr_city = city
        curr_cnt = count

if curr_city:
    print(f"{curr_city}\t{curr_cnt}")
