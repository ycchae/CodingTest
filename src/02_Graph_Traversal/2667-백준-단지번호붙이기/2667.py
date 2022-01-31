import sys
input = sys.stdin.readline

n = int(input())
arr = []
visited = [[False]*n for _ in range(n)]
for i in range(n):
    arr.append([])
    s = input().strip()
    for j in range(n):
        arr[i].append(True if s[j] == "1" else False)


from collections import deque
directions = [(-1,0), (1,0), (0,1), (0,-1)]
def bfs(row, col):
    global answer
    q = deque([(row, col)])
    visited[row][col] = True
    num_house = 1

    while q:
        pos = q.popleft()
        
        row, col = pos[0], pos[1]

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or not new_row < n or new_col < 0 or not new_col < n:
                continue

            if arr[new_row][new_col] and not visited[new_row][new_col]:
                q.append((new_row, new_col))
                num_house +=1
                visited[new_row][new_col] = True
                
    return num_house

answer = []
num_complex = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j]:
            num_complex += 1
            answer.append(bfs(i,j))
        
print(num_complex)
print('\n'.join(map(str,sorted(answer))))