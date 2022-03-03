import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

drow = [1,-1,0,0]
dcol = [0,0,1,-1]

import itertools
from collections import deque

vcnt = 0
visited = [[-1]*N for _ in range(N)]
double_loop = list(itertools.product(range(N), range(N)))

def find_move_pop():
    moved = False
    
    for _ in range(len(cand)):
        i,j = cand.popleft()
        if visited[i][j] == vcnt:
            continue
        union = []

        q = deque([(i,j)])
        visited[i][j] = vcnt
        union.append((i,j))
        total_pop = board[i][j]

        while q:
            r, c = q.popleft()

            for d in range(4):
                nr = r + drow[d]; nc = c + dcol[d]
                
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
                if visited[nr][nc] == vcnt:
                    continue
                
                diff = abs(board[r][c] - board[nr][nc])
                if diff >= L and diff <= R:
                    q.append((nr,nc))
                    visited[nr][nc] = vcnt
                    total_pop += board[nr][nc]
                    union.append((nr,nc))

        if len(union) > 1:
            moved = True
            new_pop = total_pop // len(union)
            for nation in union:
                board[nation[0]][nation[1]] = new_pop
                cand.append((nation[0],nation[1]))

    if moved:
        return True
    return False

cand = deque([(i,j) for i in range(N) for j in range(i%2,N,2)])
answer = 0
while True:
    if not find_move_pop():
        break
    vcnt += 1
    answer += 1

print(answer)