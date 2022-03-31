import sys; sys.stdin = open('d.txt', 'r')

from collections import deque

R,C,T = map(int, input().split())
board = []

machine = []
dust = dict()
answer = 0
for i in range(R):
    board.append(list(map(int, input().split())))
    for j in range(C):
        if board[i][0] == -1:
            machine.append(i)
        elif board[i][j] >= 5:
            dust[(i,j)] = board[i][j]

def move():
    r = machine[0]
    for i in range(r-1, 0, -1):
        board[i][0] = board[i-1][0]
    board[0][:C-1] = board[0][1:]
    for i in range(r):
        board[i][C-1] = board[i+1][C-1]
    board[r][1:] = [0] + board[r][1:C-1]

    r = machine[1]
    for i in range(r+1, R-1):
        board[i][0] = board[i+1][0]
    board[R-1][:C-1] = board[R-1][1:]
    for i in range(R-1, r+1, -1):
        board[i][C-1] = board[i-1][C-1]
    board[r][1:] = [0] + board[r][1:C-1]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
stop_spread = False
t = 0
while t < T:
    # 확산
    if not stop_spread:
        for dt, v in dust.items():
            r, c, = dt
            size = v
            nsize = size // 5
            cnt = 0
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nc < 0 or nr >= R or nc >= C: continue
                if nc == 0 and (nr == machine[0] or nr == machine[1]): continue

                board[nr][nc] += nsize
                cnt += 1

            board[r][c] -= nsize * cnt
    for b in board:
        print(b)
    exit()
    move()
    for b in board:
        print(b)
    input()

    if not stop_spread:
        # update dust
        dust = dict()
        for i in range(R):
            for j in range(C):
                if board[i][j] >= 5:
                    dust[(i,j)] = board[i][j]
    if not dust:
        stop_spread = True

    t += 1

answer = 0
for i in range(R):
    for j in range(C):
        answer += board[i][j]

print(answer+2)