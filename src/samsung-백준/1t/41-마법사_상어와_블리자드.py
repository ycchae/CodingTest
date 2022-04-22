import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
mdirs = [(0,-1),(1,0),(0,1),(-1,0)]
N, M = map(int, input().split())

shark = ((N+1)//2 -1, (N+1)//2 -1)
board = []
K = N*N
for i in range(N):
    board.append(list(map(int, input().split())))
    K -= board[i].count(0)
nball = K

answer = 0
def check4():
    global answer, nball
    nr, nc = shark
    l, d, cd, k = 1, 0, 0, 0
    cnt, num = 0, 0
    updated = False
    while k < K:
        for _ in range(l):
            nr = nr + mdirs[d][0]
            nc = nc + mdirs[d][1]

            if board[nr][nc] > 0:
                if num == 0:
                    check = []
                    num = board[nr][nc]
                    cnt = 1
                elif board[nr][nc] == num:
                    cnt += 1
                else:
                    if cnt >= 4:
                        nball -= cnt
                        answer += num * cnt
                        if not updated: updated = True
                        for pos in check:
                            r, c = pos
                            board[r][c] = 0
                    check = []
                    num = board[nr][nc]
                    cnt = 1
                check.append((nr,nc))

            k += 1
            if k >= K:
                if cnt >= 4:
                    nball -= cnt
                    answer += num * cnt
                    if not updated: updated = True
                    for pos in check:
                        r, c = pos
                        board[r][c] = 0
                return updated

        cd += 1
        if cd % 2 == 0:
            cd = 0
            l += 1
        d = (d + 1) % 4

    return updated

def group():
    nr, nc = shark
    l, d, cd, k = 1, 0, 0, 0
    cnt, num = 0, 0
    ngr = 0
    gr = []
    while k < K:
        for _ in range(l):
            nr = nr + mdirs[d][0]
            nc = nc + mdirs[d][1]

            if board[nr][nc] > 0:
                if num == 0:
                    num = board[nr][nc]
                    cnt = 1
                elif board[nr][nc] == num:
                    cnt += 1
                else:
                    gr.append(cnt)
                    gr.append(num)
                    ngr += 2
                    if ngr >= N*N - 1:
                        return gr

                    num = board[nr][nc]
                    cnt = 1

            k += 1
            if k >= K:
                gr.append(cnt)
                gr.append(num)
                return gr

        cd += 1
        if cd % 2 == 0:
            cd = 0
            l += 1
        d = (d + 1) % 4

    return gr

def rebuild(gr):
    global K, nball
    nr, nc = shark
    l, d, cd, k = 1, 0, 0, 0

    nboard = [[0]*N for _ in range(N)]
    K = min(len(gr), N*N-1)
    nball = K
    while k < K:
        for _ in range(l):
            nr = nr + mdirs[d][0]
            nc = nc + mdirs[d][1]
            k += 1
            if k > K: return nboard
            nboard[nr][nc] = gr[k-1]

        cd += 1
        if cd % 2 == 0:
            cd = 0
            l += 1
        d = (d + 1) % 4

    return nboard


def blizard(d, s):
    global nball
    r, c = shark
    for i in range(1, s+1):
        nr = r + dirs[d][0] * i
        nc = c + dirs[d][1] * i
        if board[nr][nc] > 0:
            board[nr][nc] = 0
            nball -= 1

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    if nball < 0: break
    blizard(d,s)

    updated = True
    while updated:
        updated = False
        if nball < 0: break
        updated = check4()

    if nball < 0: break
    gr = group()
    board = rebuild(gr)

print(answer)