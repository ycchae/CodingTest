import sys; sys.stdin = open('d.txt', 'r')

from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
day = 0

dirs = [(0,-1),(0,1),(-1,0),(1,0)]
vd = [[-1]*N for _ in range(N)]
cand = deque([(i,j) for i in range(N) for j in range(i % 2, N, 2)])

while day <= 2000:
    updated = False
    for _ in range(len(cand)):
        i,j = cand.popleft()
        if vd[i][j] == day: continue

        q = deque([(i,j)])
        vd[i][j] = day
        union = [(i,j)]
        total_pop = board[i][j]

        while q:
            r,c = q.popleft()

            for d in range(4):
                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
                if vd[nr][nc] == day: continue
                if L <= abs(board[r][c] - board[nr][nc]) <= R:
                    q.append((nr,nc))
                    vd[nr][nc] = day
                    total_pop += board[nr][nc]
                    union.append((nr,nc))

        if len(union) > 1:
            updated = True
            new_pop = total_pop // len(union)
            for i,j in union:
                board[i][j] = new_pop
                cand.append((i,j))

    if not updated: break
    day += 1

print(day)