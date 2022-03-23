import sys; input = sys.stdin.readline

N, M = map(int, input().split())

def distance(a,b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

vertex = []
for i in range(N):
    x,y = map(int, input().split())
    vertex.append((i+1, (x,y)))

edges = [[] for _ in range(N+1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    edges[v1].append((0, v2))
    edges[v2].append((0, v1))
    
for i, v1 in enumerate(vertex):
    for v2 in vertex[i+1:]:
        d = distance(v1[1],v2[1])
        edges[v1[0]].append((d,v2[0]))
        edges[v2[0]].append((d,v1[0]))

import heapq
visited = [False]*(N+1)
heap = [(0,1)]

answer = 0
visited_cnt = 0
while heap:
    if visited_cnt == N: break
    w,s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        visited_cnt += 1
        for e in edges[s]: heapq.heappush(heap, e)
    
print(f"{answer:.2f}")