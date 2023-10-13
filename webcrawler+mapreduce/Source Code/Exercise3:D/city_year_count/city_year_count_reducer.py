#!/usr/bin/env python
import sys

current_key = None
current_count = 0

# Process each line from standard input
for line in sys.stdin:
    # Split the line into key and count
    key, count = line.strip().split('\t')

    # Convert count to an integer
    count = int(count)

    # If the current key is None, or if it's different from the previous key
    if current_key is None or key != current_key:
        # If we have a current key (i.e., not the first key), output its count
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        # Set the current key and initialize the count
        current_key = key
        current_count = count
    else:
        # If the key is the same as the current key, increment the count
        current_count += count

# Output the last key and its count
if current_key is not None:
    print(f"{current_key}\t{current_count}")

