#!/usr/bin/python3

import sys

current_anime = None
animes = []

for line in sys.stdin:
    line = line.strip()
    try:
        anime1, count, anime2 = line.split('\t', 2)
        count = int(count.strip())
        if current_anime == anime1:
            animes.append(anime2)
        else:
            if current_anime:
                print(f"{current_anime}\t" + ",".join(animes[:20]))
            current_anime = anime1
            animes = [anime2]
    except:
        pass
