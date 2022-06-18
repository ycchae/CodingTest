import sys; sys.stdin = open('d.txt', 'r')

N,M,T = map(int, input().split())

machine = []
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        if board[i][j] == -1:
            machine.append((i,j))


dirs = [(0,1),(0,-1),(-1,0),(1,0)]
def spread():
    global board
    nboard = [[0]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if board[r][c] >= 5:
                get = board[r][c] // 5
                cnt = 0
                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
                    if board[nr][nc] == -1: continue
                    cnt += 1
                    nboard[nr][nc] += get
                nboard[r][c] += board[r][c] - (get * cnt)
            else:
                nboard[r][c] += board[r][c]
    
    board = nboard


def machine_on():
    # anti-clock
    r,c = machine[0]
    for i in range(r-1):
        board[r-1-i][c] = board[r-1-i -1][c]
    for j in range(M-1):
        board[0][c+j] = board[0][c+j+1]
    for i in range(r):
        board[i][M-1] = board[i+1][M-1]
    for j in range(M-2):
        board[r][M-1 - j] = board[r][M-1 -j -1]
    board[r][c+1] = 0
    # clock
    r,c = machine[1]
    for i in range(N-r-2):
        board[r+1+i][c] = board[r+1+i+1][c]
    for j in range(M-1):
        board[N-1][c+j] = board[N-1][c+j+1]
    for i in range(N-r-1):
        board[N-1-i][M-1] = board[N-1-i-1][M-1]
    for j in range(M-2):
        board[r][M-1 - j] = board[r][M-1 -j -1]
    board[r][c+1] = 0


for _ in range(T):
    spread()
    machine_on()

answer = 2
for b in board:
    answer += sum(b)
print(answer)