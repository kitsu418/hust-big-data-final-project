#!/usr/bin/python3

from ast import arg
import sys

recommends = {}

with open ("datas/recommendation-data", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        anime, recommend = line.split('\t', 1)
        recommend = recommend.split(',')
        recommends[anime] = recommend

for argument in sys.stdin:
    argument = argument.strip()
    if argument not in recommends:
        print("Error: anime not found!")
    else:
        for (i, recommend) in enumerate(recommends[argument]):
            print(f"#{i + 1}: {recommend}")
