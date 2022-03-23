import sys; input = sys.stdin.readline

N = int(input())
root = [i for i in range(N)]

def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]

edges = []
for i in range(N):
    for j,v in enumerate(list(map(int, input().split()))):
        edges.append((i,j,v))
edges.sort(key=lambda x: x[2])

answer, cnt = 0, 0
for s,e,w in edges:
    sroot = find(s)
    eroot = find(e)
    if sroot != eroot:
        cnt += 1
        if sroot < eroot: root[eroot] = sroot
        else: root[sroot] = eroot
        answer += w
    if cnt == N-1: break
print(answer)

# Prim
# N = int(input())
# edges = [[] for _ in range(N)]
# for i in range(N):
#     for j,v in enumerate(list(map(int, input().split()))):
#         edges[i].append((v, j))
#         edges[j].append((v, i))
        

# import heapq

# heap = [(0, 1)]
# vcnt = 0
# visited = [False]*N
# answer = 0
# while heap:
#     if vcnt == N: break
#     w, s = heapq.heappop(heap)
#     if not visited[s]:
#         answer += w
#         visited[s] = True
#         vcnt += 1
#         for w2, e in edges[s]:
#             heapq.heappush(heap, (w2, e))
# print(answer)        
