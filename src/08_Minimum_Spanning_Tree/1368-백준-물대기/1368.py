N = int(input())

edges = []
for i in range(N): edges.append((0,i+1,int(input())))
for i in range(N):
    for j, v in enumerate(list(map(int, input().split()))):
        if i+1 == j+1: continue
        edges.append((i+1,j+1,v))
        
edges.sort(key=lambda x: x[2])

root = [i for i in range(N+1)]
def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]

answer = 0
vcnt = 0
for s,e,w in edges:
    sroot = find(s)
    eroot = find(e)
    if sroot != eroot:
        if sroot < eroot: root[eroot] = sroot
        else: root[sroot] = eroot
        vcnt += 1
        answer += w
        if vcnt == N: break
        
print(answer)