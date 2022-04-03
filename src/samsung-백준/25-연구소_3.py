import sys; sys.stdin = open('d.txt', 'r')

from collections import deque
N, M = map(int, input().split())
MAX = N*N

board = []
viruses = []
nwalls = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 2:
            viruses.append((i,j,0))
        elif board[i][j] == 1:
            nwalls += 1

nvirus = len(viruses)
target = N*N - nwalls - nvirus

selected = []
dirs = [(0,1),(0,-1),(-1,0),(1,0)]
def bfs():
    dq = deque(selected)

    visited = [[False]*N for _ in range(N)]
    for s in selected:
        r, c, _ = s
        visited[r][c] = True

    cnt = 0
    while dq:
        r, c, t = dq.popleft()
        if t >= answer: return MAX
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visited[nr][nc]: continue
            if board[nr][nc] == 1: visited[nr][nc] = True; continue

            if board[nr][nc] == 0: cnt += 1
            visited[nr][nc] = True
            dq.append((nr,nc,t+1))

        if cnt == target:
            return t+1

    return MAX

answer = MAX
def dfs(cur, depth):
    global answer
    if depth == M:
        res = bfs()
        if answer > res: answer = res
        return

    for i in range(cur+1, nvirus):
        selected.append(viruses[i])
        dfs(i, depth+1)
        selected.pop()

if target == 0: print(0); exit(0)
dfs(-1, 0)

if answer == MAX: print(-1)
else: print(answer)