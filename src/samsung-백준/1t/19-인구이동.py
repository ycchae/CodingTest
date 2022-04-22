import sys; sys.stdin = open('d.txt', 'r')

from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited= [[-1]*N for _ in range(N)]

dirs = [(1,0),(-1,0),(0,-1),(0,1)]

def update(day):
    updated = False
    for _ in range(len(cand)):
        i, j = cand.popleft()
        if visited[i][j] == day: continue
        q = [(i,j)]
        visited[i][j] = day
        union = [(i,j)]
        s = board[i][j]
        while q:
            r,c = q.pop()
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
                if visited[nr][nc] == day: continue
                if L <= abs(board[r][c] - board[nr][nc]) <= R:
                    q.append((nr,nc))
                    visited[nr][nc] = day
                    union.append((nr,nc))
                    s += board[nr][nc]

        if len(union) >= 2:
            if not updated: updated = True
            avg = s // len(union)
            for r, c in union:
                board[r][c] = avg
                cand.append((r,c))

    return updated

cand = deque([(i,j) for i in range(N) for j in range(i%2, N, 2)])
day = 0
while True:
    if not update(day): break
    day += 1
print(day)