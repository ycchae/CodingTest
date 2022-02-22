import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = sys.maxsize

def dfs(start, cur):
    global answer
    global cost

    if all(visited):
        if board[cur][start] != 0: answer = min(answer, cost + board[cur][start])
        return
    
    for i in range(N):
        if board[cur][i] != 0 and not visited[i] and cost < answer:
            visited[i] = True
            cost += board[cur][i]
            dfs(start, i)
            cost -= board[cur][i]
            visited[i] = False


cost = 0
visited = [False] * N
for start in range(N):
    visited[start] = True
    dfs(start, start)
    visited = [False] * N

print(answer)