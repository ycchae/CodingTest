## Kruskal
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
root = [i for i in range(V+1)]
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]

answer = 0
for s, e, w in edges:
    sroot = find(s)
    eroot = find(e)
    if sroot != eroot:
        if sroot > eroot:
            root[sroot] = eroot
        else:
            root[eroot] = sroot
        answer += w
print(answer)

## Prim
# import sys
# import heapq
# input = sys.stdin.readline

# V, E = map(int, input().split())
# visited = [False] * (V+1)
# edges = [[] for _ in range(V+1)]
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     edges[s].append((w,e))
#     edges[e].append((w,s))

# heap = [(0, 1)]
# answer = 0
# cnt = 0
# while heap:
#     if cnt == V: break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         answer += w
#         visited[s] = True
#         cnt += 1
#         for e in edges[s]: heapq.heappush(heap, e)

# print(answer)