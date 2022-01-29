import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    i,j = map(int, input().split())
    graph[j].append(i)

def bfs(start):
    q = deque([start])
    visited = [False for _ in range(n+1)]
    visited[start] = True
    hacked = 1

    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                hacked += 1
    return hacked

max_hacked = 0
for i in range(1, n+1):
    if not len(graph[i]): continue
    hacked = bfs(i)
    if max_hacked <= hacked:
        if max_hacked < hacked: 
            max_hacked = hacked
            answer = []
        answer.append(i)
    
print(*answer)
