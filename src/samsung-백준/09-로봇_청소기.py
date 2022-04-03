N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

rds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# 북동남서
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

from collections import deque

clean = dict()
dq = deque([(r, c, d)])

while dq:
    r, c, d = dq.popleft()
    board[r][c] = 2
    clean[(r, c)] = True
    gone = False
    for i in range(1, 5):
        nd = (d - i) % 4
        nr = r + ds[nd][0]
        nc = c + ds[nd][1]
        # if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
        if board[nr][nc] != 0: continue
        dq.append((nr, nc, nd))
        gone = True
        break

    if not gone:
        nr = r + rds[d][0]
        nc = c + rds[d][1]
        if board[nr][nc] == 1: break
        dq.append((nr, nc, d))

print(len(clean))
