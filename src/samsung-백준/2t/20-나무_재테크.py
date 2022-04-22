import sys; sys.stdin = open('d.txt', 'r')

N, M, K = map(int, input().split())
nutrition = [[5]*N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]

trees = [ [[] for _ in range(N)] for _ in range(N) ]
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

spread = []
def spring_summer():
    global spread
    spread = []
    for r in range(N):
        for c in range(N):
            trees[r][c].sort()
            ntree = []
            dead = 0
            for age in trees[r][c]:
                if age <= nutrition[r][c]:
                    nutrition[r][c] -= age
                    ntree.append(age+1)
                    if (age + 1) % 5 == 0:
                        spread.append((r,c))
                else:
                    dead += age // 2
            nutrition[r][c] += dead
            trees[r][c] = ntree

dirs = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]

def fall():
    for r,c in spread:
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            trees[nr][nc].append(1)

def winter():
    for r in range(N):
        for c in range(N):
            nutrition[r][c] += A[r][c]

for _ in range(K):
    spring_summer()
    fall()
    winter()

answer = 0
for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])

print(answer)
