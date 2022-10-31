#!/usr/bin/python3

import sys

current_pair = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        anime1, anime2, count = line.split('\t', 2)
        count = int(count.strip())
        if current_pair == [anime1, anime2]:
            current_count += count
        else:
            if current_pair:
                print(f"{anime1}\t{anime2}\t{current_count}")
            current_count = count
            current_pair = [anime1, anime2]
    except:
        pass
