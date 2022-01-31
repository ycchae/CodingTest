import sys
input = sys.stdin.readline
N, M = map(int, input().split())

from itertools import combinations

empties = []
viruses = []
visited = [ [False]*M for _ in range(N) ]
def init_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

board = []
for i in range(N):
    board.append([])
    for j, val in enumerate(map(int, input().split())):
        board[i].append(val)
        if val == 0:
            empties.append((i,j))
        elif val == 2:
            viruses.append((i,j))

drow = [1,-1,0,0]
dcol = [0,0,1,-1]

from collections import deque
import copy
def find_safe_room(comb):
    q = deque(viruses)
    
    new_board = copy.deepcopy(board)
    for cb in comb:
        r, c = cb[0], cb[1]
        new_board[r][c] = 1
    
    while q:
        elem = q.popleft()
        r, c = elem[0], elem[1]

        for d in range(4):
            nr = r + drow[d]
            nc = c + dcol[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if new_board[nr][nc] == 0 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
                new_board[nr][nc] = 2
    
    safe = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                safe += 1

    init_visited()
    return safe


answer = 0
for comb in combinations(empties, 3):
    num_room = find_safe_room(comb)
    answer = max(answer, num_room)

print(answer)
