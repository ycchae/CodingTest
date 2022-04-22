import sys; sys.stdin = open('../d.txt', 'r')

N, M = map(int, input().split())

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

empty = -2
board = []
black = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == -1: black += 1


def find_group():
    group = dict()
    select = []
    si = -1

    visited = [[False]*N for _ in range(N)]
    nvfalse = N*N
    max_size = 1
    for r in range(N):
        for c in range(N):
            color = board[r][c]
            if color < 1: continue
            if visited[r][c]: continue

            visited[r][c] = True
            nvfalse -= 1

            add = True
            g = [(r,c)]
            size = 1
            rainbow = []
            cand_g = [(r,c)]
            while g:
                if size + (nvfalse - black) < max_size: add = False; break
                i,j = g.pop()
                for d in dirs:
                    ni = i + d[0]
                    nj = j + d[1]
                    if ni < 0 or nj < 0 or ni >= N or nj >= N: continue
                    if visited[ni][nj]: continue
                    if board[ni][nj] == color or board[ni][nj] == 0:
                        visited[ni][nj] = True
                        nvfalse -= 1

                        if board[ni][nj] == 0:
                            rainbow.append((ni,nj))

                        size += 1
                        g.append((ni,nj))
                        cand_g.append((ni,nj))

            if len(cand_g) > 1 and add:
                si += 1
                if size > max_size: max_size = size
                select.append((-size, -len(rainbow), -r, -c, si))
                group[si] = cand_g

                for pos in rainbow:
                    i,j = pos
                    visited[i][j] = False
                    nvfalse += 1

    if si > -1:
        select.sort()
        for pos in group[select[0][-1]]:
            r,c = pos
            board[r][c] = empty

        return len(group[select[0][-1]]) ** 2

    return si

def gravity():
    for c in range(N):
        col = {N-1:[]}
        bot = N-1
        for r in range(N-1,-1,-1):
            color = board[r][c]
            if color >= 0:
                col[bot].append(color)
            elif color == -1:
                bot = r
                col[bot] = [-1]

        for r in range(N):
            board[r][c] = empty

        for bot, colors in col.items():
            for i, color in enumerate(colors):
                board[bot - i][c] = color

def rotate():
    global board
    tmpb = [[empty]*N for _ in range(N)]
    for r in range(N):
        for nr in range(N):
            tmpb[N-1-nr][r] = board[r][nr]
    board = tmpb


answer = 0
while True:
    res = find_group()
    if res < 0: break
    answer += res
    gravity()
    rotate()
    gravity()

print(answer)