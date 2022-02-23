import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)
N = int(input())
root = [i for i in range(N)]
M = int(input())

def find(x):
    if x != root[x]: root[x] = find(root[x])
    return root[x]
def union(a,b):
    a, b = find(a), find(b)
    if a != b: root[b] = a

for i in range(N):
    road = list(map(int, input().split()))
    for j, val in enumerate(road):
        if val: union(i, j)

travel = list(map(int, input().split()))
if len(set([find(i-1) for i in travel])) != 1: print('NO')
else: print('YES')