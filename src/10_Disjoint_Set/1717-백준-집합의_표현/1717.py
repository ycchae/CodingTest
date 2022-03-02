import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
root = [i for i in range(n+1)]

def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]

def union(a,b):
    a, b = find(a), find(b)
    if a != b: root[b] = a

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        if find(a) == find(b): print('YES')
        else: print('NO')
    else: union(a,b)