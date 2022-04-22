import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dice = [
    [0,2,0],
    [4,1,3],
    [0,5,0],
    [0,6,0],
]

def get_nd(d, a, b):
    if a > b:
        return (d + 1) % 4
    elif a < b:
        return (d - 1) % 4
    else:
        return d

def get_score(r,c,b):
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True
    q = [(r,c)]
    score = 1

    while q:
        r,c = q.pop()
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if visited[nr][nc]: continue
            if board[nr][nc] == b:
                visited[nr][nc] = True
                q.append((nr,nc))
                score += 1
    return score * b

def get_bottom(d):
    global dice
    ndice = [[0]*3 for _ in range(4)]
    # top, battom, front, back, left, right
    if d == 0:
        # keep
        ## back
        ndice[0][1] = dice[0][1]
        ## front
        ndice[2][1] = dice[2][1]
        # top
        ndice[1][1] = dice[1][0]
        # left
        ndice[1][0] = dice[3][1]
        # right
        ndice[1][2] = dice[1][1]
        # bottom
        ndice[3][1] = dice[1][2]

    elif d == 1:
        # keep
        ## left
        ndice[1][0] = dice[1][0]
        ## right
        ndice[1][2] = dice[1][2]
        # top
        ndice[1][1] = dice[0][1]
        # front
        ndice[2][1] = dice[1][1]
        # back
        ndice[0][1] = dice[3][1]
        # bottom
        ndice[3][1] = dice[2][1]

    elif d == 2:
        # keep
        ## back
        ndice[0][1] = dice[0][1]
        ## front
        ndice[2][1] = dice[2][1]
        # top
        ndice[1][1] = dice[1][2]
        # left
        ndice[1][0] = dice[1][1]
        # right
        ndice[1][2] = dice[3][1]
        # bottom
        ndice[3][1] = dice[1][0]

    elif d == 3:
        # keep
        ## left
        ndice[1][0] = dice[1][0]
        ## right
        ndice[1][2] = dice[1][2]
        # top
        ndice[1][1] = dice[2][1]
        # front
        ndice[2][1] = dice[3][1]
        # back
        ndice[0][1] = dice[1][1]
        # bottom
        ndice[3][1] = dice[0][1]

    dice = ndice
    return dice[3][1]


answer = 0
r, c = 0, 0
d = 0
for _ in range(K):
    nr, nc = r + dirs[d][0], c + dirs[d][1]
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        d = (d + 2) % 4
        nr, nc = r + dirs[d][0], c + dirs[d][1]

    r, c = nr, nc
    a = get_bottom(d)
    b = board[r][c]

    score = get_score(r, c, b)
    d = get_nd(d, a, b)
    answer += score
print(answer)