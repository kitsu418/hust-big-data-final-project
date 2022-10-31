#!/usr/bin/python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        animes = line.split('\t')

        for i in range(len(animes)):
            for j in range(i + 1, len(animes)):
                print(f"{animes[i]}\t{animes[j]}\t1")

    except:
        pass
