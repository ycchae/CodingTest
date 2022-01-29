import sys
input = sys.stdin.readline

n = int(input())

graph = {v: [] for v in range(1, n+1)}
for _ in range(n-1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

from collections import deque

answer = [0] * (n+1)
def bfs(s):
    q = deque([s])
    visited = [False]*(n+1)
    visited[s] = True
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                answer[w] = v

bfs(1)
for x in answer[2:]:
    print(x)