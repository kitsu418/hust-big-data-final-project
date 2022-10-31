#!/usr/bin/python3

import sys

anime_map = {}

with open("datas/anime.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        anime = line.strip()
        try:
            info = line.split(',')
            if info[0] == 'anime_id':
                continue
            anime_map[info[0]] = info[1]
        except:
            pass

with open("datas/raw-recommendation-data", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        main_anime, animes = line.split('\t', 1)
        animes = animes.split(',')
        if main_anime in anime_map:
            print(f"{anime_map[main_anime]}\t" + ",".join(
                map(lambda x: anime_map[x], filter(lambda x: x in anime_map, animes))))
