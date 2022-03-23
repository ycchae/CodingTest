from collections import defaultdict
import sys; input = sys.stdin.readline

MAX=sys.maxsize

V, E = map(int, input().split())
houses = [True] * (V+1)
graph = defaultdict(dict)
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w
    
m,x = map(int, input().split())
ms = list(map(int, input().split()))
for mm in ms:
    graph[0][mm] = 0
    houses[mm] = False
    
s,y = map(int, input().split())
sbs = list(map(int, input().split()))
for sb in sbs:
    graph[V+1][sb] = 0
    houses[sb] = False

import heapq

def dijkstra(graph, start, criteria):
    distances = {v: MAX for v in range(V+2)}
    distances[start] = 0
    hq = [(0, start)]
    while hq:
        cdist, v = heapq.heappop(hq)
        if distances[v] < cdist: continue
        for w, ndist in graph[v].items():
            tdist = cdist + ndist
            if tdist < criteria:
                if tdist < distances[w]:
                    distances[w] = tdist
                    heapq.heappush(hq, (tdist, w))
    return distances

d1 = dijkstra(graph, 0, x)
d2 = dijkstra(graph, V+1, y)
answer = MAX
for i in range(1, V+1):
    if not houses[i]: continue
    if answer > d1[i]+d2[i]: answer = d1[i]+d2[i]

if answer == MAX: print(-1)
else: print(answer)