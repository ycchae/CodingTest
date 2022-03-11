from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def divide(group, r,c,d1,d2):
    for i in range(d1+1):
        group[r+i][c-i] = 5
        group[r+d2+i][c+d2-i] = 5

    for i in range(d2+1):
        group[r+i][c+i] = 5
        group[r+d1+i][c-d1+i] = 5

    for i in range(0, r+d1):
        for j in range(0, c+1):
            if group[i][j] == 5: break
            group[i][j] = 1
    for i in range(0, r+d2+1):
        for j in range(N-1, c+1-1, -1):
            if group[i][j] == 5: break
            group[i][j] = 2
    for i in range(r+d1, N):
        for j in range(0, c-d1+d2):
            if group[i][j] == 5: break
            group[i][j] = 3
    for i in range(N-1, r+d2+1-1, -1):
        for j in range(N-1, c-d1+d2-1, -1):
            if group[i][j] == 5: break
            group[i][j] = 4

    populations = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if group[i][j] == 0: group[i][j] = 5
            populations[group[i][j]] += board[i][j]
    
    vals = [populations[1], populations[2], populations[3], populations[4], populations[5]]
    ret = max(vals) - min(vals)

    return ret

for r in range(N-2):
    for c in range(1, N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                # top left right bottom
                bpoints = [(r, c), (r+d1, c-d1), (r+d2, c+d2), (r+d1+d2, c-d1+d2)]
                if any(x[0] < 0 or x[1] < 0 or x[0] >= N or x[1] >= N for x in bpoints): continue
                group = [[0]*N for _ in range(N)]
                ret = divide(group, r, c, d1, d2)
                if ret < answer: answer = ret
print(answer)