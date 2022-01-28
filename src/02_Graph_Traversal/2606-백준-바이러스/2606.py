import sys
input = sys.stdin.readline

n = int(input())
conn = int(input())

d = {i:set() for i in range(1, n+1)}
for _ in range(conn):
    i, j = map(int, input().split())
    d[i].add(j)
    d[j].add(i)

answer = 0
visited = set()

def dfs(i):
    for j in d[i]:
        if j not in visited:
            visited.add(j)
            dfs(j)

dfs(1)
print(len(visited)-1)