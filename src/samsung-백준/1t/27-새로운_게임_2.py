from collections import defaultdict
import sys; input = sys.stdin.readline
white, red, blue = 0, 1, 2
directions= [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
criteria = 4

def flip_dir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    if d == 4: return 3

N, K = map(int, input().split())
board = defaultdict(int) # 위치
b = []
for i in range(N+2):
    if not(i == 0 or i == N+1): b = list(map(int, input().split()))
    for j in range(N+2):
        if i == 0 or i == N+1 or j == 0 or j == N+1: board[(i,j)] = blue
        else: board[(i,j)] = b[j-1]

horse_pos = []
horse_dir = []
status = defaultdict(list) # 위치
for i in range(K):
    r,c,d = map(int, input().split())
    horse_pos.append((r,c))
    horse_dir.append(d)
    status[(r,c)].append(i)

answer = 0
while True:
    answer += 1
    if answer > 1000: print(-1); exit(0)

    for cur in range(K):
        r,c = horse_pos[cur]
        d = horse_dir[cur]
        nr, nc = r + directions[d][0], c + directions[d][1]

        color = board[(nr,nc)]
        idx = status[(r,c)].index(cur)
        move_targets = status[(r,c)][idx:]

        if color == blue:
            d = horse_dir[cur] = flip_dir(horse_dir[cur])
            nr, nc = r + directions[d][0], c + directions[d][1]
            ncolor = board[(nr,nc)]
            if ncolor == blue: continue

        for t in move_targets: horse_pos[t] = (nr,nc)

        if color == white or (color == blue and ncolor == white):
            status[(nr,nc)].extend(move_targets)
        if color == red or (color == blue and ncolor == red):
            status[(nr,nc)].extend(reversed(move_targets))

        if len(status[(nr,nc)]) >= criteria: print(answer); exit(0)

        status[(r,c)] = status[(r,c)][:idx]