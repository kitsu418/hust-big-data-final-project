#!/usr/bin/python3

import sys

animes = []
current = None

for line in sys.stdin:
    try:
        line = line.strip()
        datas = line.split(',')
        if datas[0] == 'user_id':
            continue
        elif datas[0] == current:
            animes.append(datas[1])
        else:
            if current and len(animes) >= 10:
                animes.sort(key=int)
                print('\t'.join(animes))
            current = datas[0]
            animes = [datas[1]]

    except:
        pass
