import sys; sys.stdin = open('../d.txt', 'r')

N, M, K = map(int, input().split())

checkpoint = []
heater = []

# 0우 1좌 2상 3하
dirs = [(0,1),(0,-1),(-1,0),(1,0)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 5:
            checkpoint.append((i,j))
        elif line[j] > 0:
            heater.append((i,j,line[j]-1))

board = [[0]*M for _ in range(N)]

walls = dict()
# wall d0: 위쪽
# wall d1: 오른쪽
for _ in range(int(input())):
    r,c,d = map(int, input().split())
    walls[(r-1,c-1,d)] = True

def wall_check(r, c, d):
    if d == 0:
        if walls.get((r,c,1)): return True
    elif d == 1:
        if walls.get((r, c-1, 1)): return True
    elif d == 2:
        if walls.get((r,c,0)): return True
    elif d == 3:
        if walls.get((r+1,c,0)): return True
    return False


def heater_on():
    visited = [[-1]*M for _ in range(N)]
    for hi, h in enumerate(heater):
        r,c,d = h

        nr = r + dirs[d][0]
        nc = c + dirs[d][1]
        board[nr][nc] += 5
        visited[nr][nc] = hi
        q = [(nr,nc,5)]
        while q:
            r,c,power = q.pop()
            if power == 1: continue

            # straight
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if visited[nr][nc] != hi and not wall_check(r,c, d):
                visited[nr][nc] = hi
                board[nr][nc] += power -1
                q.append((nr,nc,power-1))

            # diags
            if d < 2: dgs = [2,3]
            else: dgs = [0,1]
            for nd in dgs:
                nr1 = r + dirs[nd][0]
                nc1 = c + dirs[nd][1]
                if nr1 < 0 or nc1 < 0 or nr1 >= N or nc1 >= M: continue
                if wall_check(r,c,nd): continue

                nr2 = nr1 + dirs[d][0]
                nc2 = nc1 + dirs[d][1]
                if nr2 < 0 or nc2 < 0 or nr2 >= N or nc2 >= M: continue
                if visited[nr2][nc2] == hi: continue
                if wall_check(nr1, nc1, d): continue

                visited[nr2][nc2] = hi
                board[nr2][nc2] += power -1
                q.append((nr2,nc2,power-1))


def calibrate():
    nboard = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            for d in [0, 3]:
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]
                if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
                if wall_check(r,c,d): continue
                if board[r][c] > board[nr][nc]:
                    get = (board[r][c] - board[nr][nc]) // 4
                    nboard[nr][nc] += get
                    nboard[r][c] -= get
                elif board[r][c] < board[nr][nc]:
                    get = (board[nr][nc] - board[r][c]) // 4
                    nboard[nr][nc] -= get
                    nboard[r][c] += get

            nboard[r][c] += board[r][c]
    return nboard


def decrease():
    for j in range(M):
        if board[0][j] > 0: board[0][j] -= 1
        if board[N-1][j] > 0: board[N-1][j] -= 1
    for i in range(1,N-1):
        if board[i][0] > 0: board[i][0] -= 1
        if board[i][M-1] > 0: board[i][M-1] -= 1

def check_temperature():
    for r, c in checkpoint:
        if board[r][c] < K:
            return False
    return True

choco = 0
while choco <= 100:
    heater_on()
    board = calibrate()
    decrease()
    choco += 1
    if choco == 101: break
    if check_temperature(): break

print(choco)