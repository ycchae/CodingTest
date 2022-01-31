import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
visited = []
for i in range(n):
    arr.append([])
    visited.append([])
    s = input().strip()
    for j in range(m):
        arr[i].append(True if s[j] == "1" else False)
        visited[i].append(False)

answer = sys.maxsize

from collections import deque
directions = [(-1,0), (1,0), (0,1), (0,-1)]
def bfs(row, col):
    global answer
    q = deque([(row, col, 1)])
    visited[row][col] = True

    while q:
        pos = q.popleft()
        row, col, c = pos[0], pos[1], pos[2]

        if c > answer:
            continue
        if row == n-1 and col == m-1:
            if answer > c:
                answer = c
            continue

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or not new_row < n or new_col < 0 or not new_col < m:
                continue

            if arr[new_row][new_col] and not visited[new_row][new_col]:
                q.append((new_row, new_col, c+1))
                visited[new_row][new_col] = True
                

bfs(0,0)
print(answer)