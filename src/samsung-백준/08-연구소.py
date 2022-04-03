from collections import deque
from itertools import combinations
import sys; input = sys.stdin.readline

N,M = map(int, input().split())
empty = []
virus = []
walls = {}
ow = 0

directions = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(N):
    for j, v in enumerate(list(map(int, input().split()))):
        if v == 0: empty.append((i,j))
        elif v == 2: virus.append((i,j))
        elif v == 1: walls[(i,j)] = True; ow += 1

answer = 0
for comb in combinations(empty, 3):
    for wall in comb: walls[(wall[0], wall[1])] = True
    
    dq = deque(virus)
    visited = dict()
    for v in virus: visited[(v[0],v[1])] = True

    while dq:
        r,c = dq.popleft()
        for d in directions:
            nr,nc = r + d[0], c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if visited.get((nr,nc)): continue
            if walls.get((nr,nc)): continue
            
            visited[(nr,nc)] = True
            dq.append((nr,nc))
    
    safe = N*M - len(visited) - ow -3
    if answer < safe: answer = safe

    for wall in comb: walls[(wall[0], wall[1])] = False
    
print(answer)