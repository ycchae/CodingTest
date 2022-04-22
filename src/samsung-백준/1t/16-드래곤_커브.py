import sys; sys.stdin = open('../d.txt', 'r')

from collections import defaultdict

directions = [(0,1),(-1,0),(0,-1),(1,0)]

N = int(input())
board = defaultdict(bool)
for _ in range(N):
    c,r,d,g = map(int, input().split())
    board[(r,c)] = True
    nr = r + directions[d][0]
    nc = c + directions[d][1]
    board[(nr,nc)] = True
    ds = [d]

    for _ in range(g):
        rds = reversed(ds)
        for rd in rds:
            nd = (rd+1)%4
            nr, nc = nr + directions[nd][0], nc + directions[nd][1]
            board[(nr,nc)] = True
            ds.append(nd)

answer = 0
keys = list(board.keys())
for k in keys:
    r,c = k
    if board[(r+1,c)] and board[(r,c+1)] and board[(r+1,c+1)]: answer += 1

print(answer)