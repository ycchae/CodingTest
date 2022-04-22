import sys; sys.stdin = open('../d.txt', 'r')

import heapq

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
N, M, K = map(int, input().split())

board = []
smells = [[[0,0] for _ in range(N)] for _ in range(N)]
shark_pos = [0]*(M+1)
shark_prio = [dict() for _ in range(M+1)]
for i in range(N):
    board.append([])
    line = list(map(int, input().split()))
    for j in range(N):
        sn = line[j]
        if sn != 0:
            shark_pos[sn] = [i,j]
            smells[i][j] = [sn, K]
            board[i].append([sn])
        else:
            board[i].append([])

for sn, d in enumerate(list(map(int, input().split()))):
    shark_pos[sn+1].append(d-1)

for sn in range(1,M+1):
    for i in range(4):
        shark_prio[sn][i] = tuple(map(lambda x: x-1, map(int, input().split())))

nshark = M
t = 0
while t < 1001:
    # shark move
    for sn in range(1, M+1):
        pos = shark_pos[sn]
        if pos == [-1,-1,-1]: continue
        r,c,d = pos
        board[r][c].remove(sn)
        prios = shark_prio[sn][d]

        moved = False
        cango = 0
        for nd in prios:
            nr = r + dirs[nd][0]
            nc = c + dirs[nd][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if cango == 0 and smells[nr][nc][0] == sn:
                cango = [nr,nc,nd]
            if smells[nr][nc][1] == 0:
                heapq.heappush(board[nr][nc], sn)
                shark_pos[sn] = [nr, nc, nd]
                moved = True
                break
        if moved: continue

        nr, nc, nd = cango
        heapq.heappush(board[nr][nc], sn)

        shark_pos[sn] = [nr, nc, nd]

    # smell del
    for i in range(N):
        for j in range(N):
            if smells[i][j][1] - 1 <= 0:
                smells[i][j] = [0, 0]
            else:
                smells[i][j][1] -= 1

    # shark del, update smells
    for i in range(N):
        for j in range(N):
            if not board[i][j]: continue
            if len(board[i][j]) > 1:
                save = heapq.heappop(board[i][j])
                for sn in board[i][j]:
                    shark_pos[sn] = [-1,-1,-1]
                    nshark -= 1
                board[i][j] = [save]
            smells[i][j] = [board[i][j][0], K]

    t += 1
    if nshark == 1: break

if t == 1001:
    t = -1

print(t)