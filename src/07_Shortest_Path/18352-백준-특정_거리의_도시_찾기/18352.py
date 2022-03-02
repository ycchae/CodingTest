import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
answer = [-1] * (N+1)
answer[X] = 0

from collections import deque
dq = deque()
graph = dict()
for _ in range(M):
    s, e = map(int, input().split())
    if not graph.get(s): graph[s] = []
    graph[s].append(e)
    if s == X:
        answer[e] = 1
        dq.append((e,1))

while dq:
    v, distance = dq.popleft()
    if not graph.get(v): continue
    for next_v in graph[v]:
        if answer[next_v] == -1:
            answer[next_v] = distance +1
            dq.append((next_v, distance +1))

for i in range(N+1):
    if answer[i] == K:
        print(i)
if K not in answer:
    print(-1)