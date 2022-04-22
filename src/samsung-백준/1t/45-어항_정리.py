import sys; sys.stdin = open('../d.txt', 'r')

C, K = map(int, input().split())

R = C
board = [[0]*C for _ in range(R-1)]
board.append(list(map(int, input().split())))

def check():
    max_fish = 0
    min_fish = 10_001
    for j in range(C):
        if min_fish > board[R - 1][j]:
            min_fish = board[R - 1][j]
        if max_fish < board[R - 1][j]:
            max_fish = board[R - 1][j]

    if max_fish - min_fish <= K:
        return True
    return False

def add():
    mins = []
    min_fish = 10_001
    for j in range(C):
        if min_fish > board[R-1][j]:
            min_fish = board[R-1][j]
            mins = [j]
        elif min_fish == board[R-1][j]:
            mins.append(j)
    for j in mins:
        board[R-1][j] += 1

cur_height = 0
cur_c = 0
def stacking():
    global cur_c, cur_height
    height = 1
    c = -1
    cnt = 0
    while True:
        cp = []
        for h in range(height):
            cp.append([])
            c += 1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    cp[h].append(board[r][c])
                    board[r][c] = 0
                else:
                    break

        update_c = c+1
        for hr in range(height):
            nr = R-1 - height + hr
            for i, v in enumerate(cp[hr]):
                nc = update_c + i
                board[nr][nc] = v
        cur_height = height
        cur_c = update_c

        cnt += 1
        if cnt % 2 == 0:
            cnt = 0
            height += 1

        if (cnt+1) % 2 == 0:
            if height+1 > C - c - (height+1): break
        if height > C - c - height: break

dirs = [(1,0),(0,1)]
def calibrate():
    global board

    nboard = [[0]*C for _ in range(R)]

    for r in range(R-1 - cur_height, R):
        for c in range(cur_c, C):
            if board[r][c] == 0: continue
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nc < 0 or nr >= R or nc >= C: continue
                if board[nr][nc] == 0: continue
                if board[r][c] > board[nr][nc]:
                    get = (board[r][c] - board[nr][nc]) // 5
                    nboard[nr][nc] += get
                    nboard[r][c] -= get
                elif board[r][c] < board[nr][nc]:
                    get = (board[nr][nc] - board[r][c]) // 5
                    nboard[nr][nc] -= get
                    nboard[r][c] += get

            nboard[r][c] += board[r][c]

    board = nboard

def rebuild():
    global board, cur_height, cur_c

    nboard = [[0] * C for _ in range(R-1)]
    fish = []
    for c in range(cur_c, C):
        for r in range(R-1, -1, -1):
            if board[r][c] > 0:
                fish.append(board[r][c])
            else: break

    nboard.append(fish)
    board = nboard
    cur_height = 0
    cur_c = 0

def pb(text):
    print(f'---{text}---')
    for b in board:
        print(b)

def stacking2():
    global cur_c, cur_height

    c = 0
    for cut in range(1,3):
        cut_c = C // (2**cut)
        height = C // cut_c - 1
        cp = []
        for h in range(cut):
            nr = R - 1 - h
            l = []
            for j in range(cut_c):
                nc = c + j
                l.append(board[nr][nc])
                board[nr][nc] = 0
            l.reverse()
            cp.append(l)

        c += cut_c
        for h in range(cut):
            nr = R - 1 - height + h
            for j, v in enumerate(cp[h]):
                nc = c + j
                board[nr][nc] = v

    cur_c = c
    cur_height = C//(C//4) -1


answer = 0
while True:
    if check(): break
    answer += 1
    add()
    stacking()
    calibrate()
    rebuild()
    stacking2()
    calibrate()
    rebuild()

print(answer)