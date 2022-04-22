import sys; sys.stdin = open('../d.txt', 'r')

import heapq
from collections import deque, defaultdict
N = int(input())

board = []
fish = [0]*(7)

visited = defaultdict(bool)
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 9:
            dq = deque([(i,j,0)])
            board[i][j] = 0
            visited[(i,j)] = True
        elif board[i][j] > 0:
            fish[board[i][j]] += 1

sec = 0

dirs = [(-1,0),(0,-1),(0,1),(1,0)]
can = fish[1]

size = 2
ate = 0
while can > 0:
    able = []

    while dq:
        r,c,t = dq.popleft()

        if able and able[0][2] <= t: continue
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visited[(nr,nc)]: continue
            if board[nr][nc] > size: continue

            visited[(nr, nc)] = True
            if 0 < board[nr][nc] < size:
                heapq.heappush(able, (nr,nc,t+1))
            elif not able: dq.append((nr,nc,t+1))

    if able:
        r, c, t = heapq.heappop(able)
        can -= 1
        ate += 1
        sec += t
        dq = deque([(r, c, 0)])
        board[r][c] = 0
    else: break

    if ate == size:
        ate = 0
        size += 1
        if size < 8:
            can += fish[size-1]

    visited = defaultdict(bool)

print(sec)