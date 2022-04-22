import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
board = [[0] * 4 for _ in range(4)]
N = 4
answer = 0

fishes = [0] * 16
for i in range(N):
    line = list(map(int, input().split()))
    for j, f in enumerate(range(0,N*2,2)):
        fn, fd = line[f] - 1, line[f+1] - 1
        fishes[fn] = [i, j, fd]
        board[i][j] = fn
        if i == 0 and j == 0:
            shark = [i,j,fd]
            answer += fn+1
            board[i][j] = -1
            fishes[fn] = [-1,-1,-1]

def fish_move(board, fishes, shark):
    for i in range(len(fishes)):
        if fishes[i] == [-1,-1,-1]: continue
        r,c,d = fishes[i]
        for dm in range(8):
            nd = (d + dm) % 8
            nr = r + dirs[nd][0]
            nc = c + dirs[nd][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if nr == shark[0] and nc == shark[1]: continue

            if board[nr][nc] == -1:
                board[nr][nc] = i
                board[r][c] = -1
            else:
                fn = board[nr][nc]
                board[r][c] = fn
                board[nr][nc] = i

                _, _, od = fishes[fn]
                fishes[fn] = [r,c,od]

            fishes[i] = [nr,nc,nd]
            break

def cp(bd):
    t = []
    for b in bd:
        t.append(b[:])
    return t

def dfs(score, board, fishes, shark):
    global answer

    fish_move(board, fishes, shark)

    isfish = False
    r,c,d = shark
    for i in range(1,4):
        nr = r + dirs[d][0]*i
        nc = c + dirs[d][1]*i
        if nr < 0 or nc < 0 or nr >= N or nc >= N: break
        if board[nr][nc] == -1: continue
        isfish = True

        nboard = cp(board)
        nfishes = fishes[:]

        fn = nboard[nr][nc]
        nboard[nr][nc] = -1

        nd = nfishes[fn][2]
        nfishes[fn] = [-1,-1,-1]

        nshark = [nr,nc,nd]

        dfs(score + fn+1, nboard, nfishes, nshark)

    if not isfish:
        if answer < score: answer = score

dfs(answer, board, fishes, shark)
print(answer)