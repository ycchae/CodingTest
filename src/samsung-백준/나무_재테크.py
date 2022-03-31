import sys; sys.stdin = open('d.txt', 'r')

from collections import deque, defaultdict

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
board = [[5]*N for _ in range(N)]

trees = dict()
ntree = M
for _ in range(M):
    x,y,age = map(int, input().split())
    trees[(x-1, y-1)] = deque([age])


def spring_summer():
    global spread_ready
    global ntree
    spread_ready = defaultdict(int)

    keys = list(trees.keys())
    for key in keys:
        r,c = key
        val = trees[key]

        alive = []
        dead = 0
        nv = len(val)
        for i in range(nv):
            age = val[i]

            if board[r][c] < age:
                ntree -= nv - i
                dead += age//2
                for j in range(i+1, nv): dead += val[j]//2
                break
            else:
                board[r][c] -= age
                alive.append(age+1)
                if (age+1) % 5 == 0: spread_ready[key] += 1

        # 양분 추가
        board[r][c] += dead

        # key 관리
        if len(alive) == 0:
            del trees[key]
        else:
            trees[key] = deque(alive)


dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
def fall():
    global ntree
    for k,v in spread_ready.items():
        r,c = k
        for d in dirs:
            nr, nc = r + d[0], c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue

            if not trees.get((nr,nc)):
                trees[(nr,nc)] = deque([1]*v)
            else:
                for _ in range(v): trees[(nr,nc)].appendleft(1)
            ntree += v

def winter():
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]

for _ in range(K):
    if ntree == 0: break
    spring_summer()
    fall()
    winter()

print(ntree)


