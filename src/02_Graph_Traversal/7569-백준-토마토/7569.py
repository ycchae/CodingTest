import sys
input = sys.stdin.readline

M,N,H = map(int, input().split())

from collections import deque
tomato = []
riped = deque()
for h in range(H):
    tomato.append([])
    for i in range(N):
        tomato[h].append([])
        for j, v in enumerate(map(int, input().split())):
            tomato[h][i].append(v)
            if v == 1:
                riped.append((h,i,j))

directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
def bfs():
    while riped:
        t = riped.popleft()
        h, r, c = t[0], t[1], t[2]
        
        for direction in directions:
            new_h = h + direction[0]
            new_r = r + direction[1]
            new_c = c + direction[2]
            if new_h < 0 or not new_h < H or new_r < 0 or not new_r < N or new_c < 0 or not new_c < M:
                continue

            if tomato[new_h][new_r][new_c] == 0:
                riped.append((new_h, new_r, new_c))
                tomato[new_h][new_r][new_c] = tomato[h][r][c] + 1

bfs()

day = 0
for h in tomato:
    for r in h:
        for c in r:
            if c == 0:
                print(-1)
                exit(0)
        day = max(day, max(r))
print(day-1)