import sys; input = sys.stdin.readline
V,E = map(int, input().split())

import heapq
edges = []
for _ in range(E):
    a,b,c = map(lambda x: x-1, map(int, input().split()))
    c += 1
    heapq.heappush(edges, (c, a,b))

root = [i for i in range(V)]

def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]

answer = 0

while edges:
    w,s,e = heapq.heappop(edges)

    
    if find(s) != find(e):
        if root[s] < root[e]: 
            root[root[e]] = root[s]
        else: 
            root[root[s]] = root[e]
        
    
        answer += w

print(answer)