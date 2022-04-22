from collections import defaultdict
import sys; input = sys.stdin.readline

N = int(input())
K = int(input())
apples = defaultdict(bool)
for _ in range(K):
    r, c = map(lambda x: x-1, map(int, input().split()))
    apples[(r,c)] = True
M = int(input())
change = defaultdict(int)
for _ in range(M):
    sp = input().split()
    change[int(sp[0])] = -1 if sp[1] == 'L' else 1

# right down left up
ds = [(0,1),((1,0)),(0,-1),(-1,0)]

board = [[0]*N for _ in range(N)]
snake_dir = 0
head = (0,0)
tail = [(0,0)]
board[0][0] = 1

time = 0
while True:
    time += 1

    nr, nc = head[0] + ds[snake_dir][0], head[1] + ds[snake_dir][1]
    if nr < 0 or nc < 0 or nr >= N or nc >= N: break
    if board[nr][nc]: break

    if apples[(nr,nc)]: apples[(nr,nc)] = False
    else: r,c = tail.pop(0); board[r][c] = 0
    board[nr][nc] = 1

    head = (nr, nc)
    tail.append((nr,nc))

    if change[time]: snake_dir = (snake_dir + change[time]) % 4

print(time)