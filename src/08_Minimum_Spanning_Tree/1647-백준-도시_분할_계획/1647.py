import sys; input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
visited = [False] * (N+1)
edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    edges[s].append((w,e))
    edges[e].append((w,s))

answer = 0
heap = [(0,1)]
cnt = 0
max_w = 0
while heap:
    if cnt == N: break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        answer += w
        if w > max_w: max_w = w
        visited[s] = True
        cnt += 1
        for e in edges[s]: heapq.heappush(heap, e)

print(answer - max_w)