import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

ch = []
home = []
for i, pan_ in enumerate(pan):
    for j, value in enumerate(pan_):
        if value == 2:
            ch.append((i,j))
        if value == 1:
            home.append((i,j))
ch_distance = [[] for i in range(len(home))]
min_city_distance = float('inf') 
for chs in combinations(ch,M): 
    city_distance = 0 
    for i, value_home in enumerate(home): 
        min_distance = float('inf') 
        for j, value_ch in enumerate(chs): 
            distance = abs(value_home[0]-value_ch[0]) + abs(value_home[1]-value_ch[1]) 
            if min_distance>distance: 
                min_distance = distance
        city_distance += min_distance 
    if min_city_distance>city_distance: 
        min_city_distance=city_distance

print(min_city_distance) 