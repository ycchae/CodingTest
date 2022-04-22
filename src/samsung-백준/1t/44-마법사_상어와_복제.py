import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
N = 4
M, S = map(int, input().split())

board = [ [[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    board[r][c].append(d)

shark = tuple(map(lambda x: x-1, map(int, input().split())))
smell = dict()
def bound_out(r,c):
    if r < 0 or c < 0 or r >= N or c >= N: return True
    return False

def move_fish():
    global board
    nboard = [ [[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            while board[r][c]:
                d = board[r][c].pop()
                handled = False
                for i in range(8):
                    nd = (d - i) % 8
                    nr = r + dirs[nd][0]
                    nc = c + dirs[nd][1]
                    if bound_out(nr,nc): continue
                    if (nr,nc) == shark: continue
                    if smell.get((nr,nc)): continue
                    nboard[nr][nc].append(nd)
                    handled = True
                    break
                if not handled:
                    nboard[r][c].append(d)
    board = nboard

cv = [2,0,1,0,4,0,3,0]
def convert(directions):
    num = 0
    for i, d in enumerate(directions):
        num += cv[d] * (10** (3-i))
    return num

def move_shark():
    global shark
    r, c = shark
    max_cnt = -1
    candidates = []

    for d1 in [0, 2, 4, 6]:
        nr1 = r + dirs[d1][0]
        nc1 = c + dirs[d1][1]
        if bound_out(nr1,nc1): continue

        for d2 in [0, 2, 4, 6]:
            nr2 = nr1 + dirs[d2][0]
            nc2 = nc1 + dirs[d2][1]
            if bound_out(nr2, nc2): continue

            for d3 in [0, 2, 4, 6]:
                nr3 = nr2 + dirs[d3][0]
                nc3 = nc2 + dirs[d3][1]
                if bound_out(nr3, nc3): continue

                cnt = 0
                poses = {(nr1, nc1), (nr2, nc2), (nr3, nc3)}
                for p in poses:
                    i, j = p
                    cnt += len(board[i][j])

                if max_cnt < cnt:
                    max_cnt = cnt
                    num = convert([d1, d2, d3])
                    candidates = [(num, poses, (nr3,nc3))]
                elif max_cnt == cnt:
                    num = convert([d1, d2, d3])
                    candidates.append((num, poses, (nr3,nc3)))

    candidates.sort(key = lambda x: x[0])
    num, poses, last = candidates[0]
    for p in poses:
        r,c = p
        if len(board[r][c]) > 0:
            smell[(r,c)] = 3
        board[r][c] = []
    shark = last

def del_smell():
    global smell
    k = list(smell.keys())
    for r,c in k:
        smell[(r,c)] -= 1
        if smell[(r,c)] == 0:
            del smell[(r,c)]

def copy():
    global fish
    fish = []
    for r in range(N):
        for c in range(N):
            for d in board[r][c]:
                fish.append((r,c,d))

def update():
    for r,c,d in fish:
        board[r][c].append(d)

for _ in range(S):
    copy()
    move_fish()
    move_shark()
    del_smell()
    update()

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(board[r][c])
print(answer)