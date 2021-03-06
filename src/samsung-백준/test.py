import sys; sys.stdin = open('d.txt', 'r')

from collections import deque
import heapq

N = int(input())
board = []
visited = [[-1]*N for _ in range(N)]
fish = [0]*7
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if 0 < line[j] <= 6:
            fish[line[j]] += 1
        elif line[j] == 9:
            shark = (i,j)
            board[i][j] = 0

size = 2
dirs = [(-1,0),(1,0),(0,1),(0,-1)]

def eat(time):
    global shark

    r,c = shark
    visited[r][c] = time
    q = deque([(r,c,0)])
    candidates = []
    while q:
        r,c,dist = q.popleft()
        if candidates and candidates[0][0] < dist+1: continue

        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visited[nr][nc] == time: continue
            if board[nr][nc] > size: continue
            visited[nr][nc] = time
            q.append((nr,nc, dist+1))
            if 0 < board[nr][nc] < size:
                heapq.heappush(candidates, (dist+1, nr,nc, board[nr][nc]))

    print(candidates)
    if candidates:
        dist, r, c, s = candidates[0]
        board[r][c] = 0
        fish[s] -= 1

        shark = (r,c)
        return dist

    return 0


time = 0
cnt = 0
while sum(fish[:size+1]):
    res = eat(time)
    print(shark, res)
    if not res: break
    time += res

    if size < 7:
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1

print(time)