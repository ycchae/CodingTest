import sys
input = sys.stdin.readline

N, M = map(int, input().split())

from collections import deque

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def melt():
    visited = [[False] * M for _ in range(N)]
    dq = deque([(0,0)])
    visited[0][0] = True
    cnt = 0
    while dq:
        r, c = dq.popleft()
        for i in range(4):
            nr = r + drow[i]
            nc = c + dcol[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc]:
                continue

            if board[nr][nc] == 0:
                dq.append((nr,nc))
                visited[nr][nc] = True
            elif board[nr][nc] == 1:
                board[nr][nc] = 0
                visited[nr][nc] = True
                cnt += 1

    return cnt

hour = 0
num_cheese = []
while True:
    hour += 1
    num_cheese.append(melt())
    if num_cheese[-1] == 0:
        break

print(hour-1)
print(num_cheese[-2])
