import sys; sys.stdin = open('d.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def pop_diff(r,c,d1,d2):
    visited = [[0]*N for _ in range(N)]
    # 5
    visited[r][c] = 5
    for i in range(1, d1+1):
        visited[r+i][c-i] = 5
        visited[r+d2+i][c+d2-i] = 5
    for i in range(1, d2+1):
        visited[r+i][c+i] = 5
        visited[r+d1+i][c-d1+i] = 5
        
    # 1
    for i in range(r+d1):
        for j in range(c+1):
            if visited[i][j] == 5: break
            visited[i][j] = 1
    # 3 
    for i in range(r+d1,N):
        for j in range(c-d1+d2):
            if visited[i][j] == 5: break
            visited[i][j] = 3
    # 2
    for i in range(r+d2+1):
        for j in range(N-1, -1, -1):
            if visited[i][j]: break
            visited[i][j] = 2
    # 4
    for i in range(r+d2+1,N):
        for j in range(N-1, c-2, -1):
            if visited[i][j]: break
            visited[i][j] = 4
    
    pops = [0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 5
                pops[4] += board[i][j]
            else: pops[visited[i][j]-1] += board[i][j]

    return max(pops) - min(pops)

answer = N*100
for r in range(N-2):
    for c in range(1, N-1):
        for d1 in range(1, c+1):
            for d2 in range(1, N-c):
                if r + d1 + d2 >= N: continue
                res = pop_diff(r,c,d1,d2)
                if res < answer: 
                    tmp = (r,c,d1,d2)
                    answer = res
print(answer)