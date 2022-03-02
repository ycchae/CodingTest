import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
vertex = list(input().split())
edges = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    s -= 1; e -= 1
    edges[s].append((w,e))
    edges[e].append((w,s))

visited = [False] * N
v_cnt = 0
heap = [(0, 1)]
answer = 0
while heap:
    if v_cnt == N: break
    w, e = heapq.heappop(heap)
    if not visited[e]:
        visited[e] = True
        v_cnt += 1
        answer += w
        for path in edges[e]:
            if vertex[e] != vertex[path[1]]:
                heapq.heappush(heap, path)
if v_cnt != N:
    print(-1)
    exit(0)
print(answer)