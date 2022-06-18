import sys; sys.stdin = open('d.txt', 'r')

N, M, K = map(int, input().split())
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

board = []
sharks = [0]*M
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        shark = line[j]-1
        if shark >= 0:
            sharks[shark] = (i,j)

for i, d in enumerate(list(map(int, input().split()))):
    sharks[i] += (d,)

prio = [dict() for _ in range(M)]

