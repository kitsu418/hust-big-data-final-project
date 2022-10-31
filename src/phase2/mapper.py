#!/usr/bin/python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        anime1, anime2, count = line.split('\t', 2)
        count = int(count)

        print(f"{anime1}\t{count}\t{anime2}")
        print(f"{anime2}\t{count}\t{anime1}")

    except:
        pass
