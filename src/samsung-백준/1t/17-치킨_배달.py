import sys; sys.stdin = open('../d.txt', 'r')

N, M = map(int, input().split())
house = []
chicken = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i,j))
        elif line[j] == 2:
            chicken.append((i,j))

nchicken = len(chicken)
select = []
max = int(1e9)
answer = max

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def dfs(cur, depth):
    global answer
    if depth == M:
        cdistance = 0
        for h in house:
            ld = max
            for s in select:
                d = distance(h,s)
                if ld > d: ld = d
            cdistance += ld

        if answer > cdistance: answer = cdistance
        return

    for c in range(cur+1, nchicken):
        select.append(chicken[c])
        dfs(c, depth+1)
        select.pop()

dfs(-1, 0)
print(answer)