from copy import deepcopy
import sys; input = sys.stdin.readline

ncount = 0
answer = -1

N = int(input())
board = []
for _ in range(N):
    l = list(map(int, input().split()))
    ncount += N - l.count(0)
    answer = max(answer, max(l))
    board.append(l)

def move(d, tboard):
    global ncount

    if d == 0: # up
        for j in range(N):
            i = 0
            size0 = 0
            while i < N:
                if tboard[i][j] == 0:
                    for k in range(i+1+size0, N):
                        if tboard[k][j] != 0: tboard[i][j] = tboard[k][j]; tboard[k][j] = 0; size0 = k-i-1; i -= 1; break
                else:
                    for k in range(i+1, N):
                        if tboard[k][j] != 0 and tboard[k][j] != tboard[i][j]: break
                        if tboard[i][j] == tboard[k][j]:
                            tboard[i][j] *= 2
                            ncount -= 1
                            tboard[k][j] = 0
                            break
                i += 1
    elif d == 1: #down
        for j in range(N):
            i = N-1
            size0 = 0
            while i >= 0:
                if tboard[i][j] == 0:
                    for k in range(i-1-size0, -1, -1):
                        if tboard[k][j] != 0: tboard[i][j] = tboard[k][j]; tboard[k][j] = 0; size0 = i-k-1; i += 1; break
                else:
                    for k in range(i-1, -1, -1):
                        if tboard[k][j] != 0 and tboard[k][j] != tboard[i][j]: break
                        if tboard[i][j] == tboard[k][j]:
                            tboard[i][j] *= 2
                            ncount -= 1
                            tboard[k][j] = 0
                            break
                i -= 1
    elif d == 2: # left
        for i in range(N):
            j = 0
            size0 = 0
            while j < N:
                if tboard[i][j] == 0:
                    for k in range(j+1+size0, N):
                        if tboard[i][k] != 0: tboard[i][j] = tboard[i][k]; tboard[i][k] = 0; size0 = k-j-1; j -= 1; break
                else:
                    for k in range(j+1, N):
                        if tboard[i][k] != 0 and tboard[i][k] != tboard[i][j]: break
                        if tboard[i][j] == tboard[i][k]:
                            tboard[i][j] *= 2
                            ncount -= 1
                            tboard[i][k] = 0
                            break
                j += 1
    elif d == 3: # right
        for i in range(N):
            j = N-1
            size0 = 0
            while j >= 0:
                if tboard[i][j] == 0:
                    for k in range(j-1-size0, -1, -1):
                        if tboard[i][k] != 0: tboard[i][j] = tboard[i][k]; tboard[i][k] = 0; size0 = j-k-1; j += 1; break
                else:
                    for k in range(j-1, -1, -1):
                        if tboard[i][k] != 0 and tboard[i][k] != tboard[i][j]: break
                        if tboard[i][j] == tboard[i][k]:
                            tboard[i][j] *= 2
                            ncount -= 1
                            tboard[i][k] = 0
                            break
                j -= 1        

# 2240 ms
# moves = [-1]*5
# def dfs(depth):
#     global answer
#     if ncount == 1 or depth == 5:    
#         tboard = deepcopy(board)
        
#         for m in moves: move(m, tboard)
#         for i in range(N): answer = max(answer, max(tboard[i]))
#         return

#     for d in range(4):
#         moves[depth] = d
#         dfs(depth+1)
# dfs(0)

# 912 ms
def dfs(board, depth):
    global answer
    if ncount == 1 or depth == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    for d in range(4):
        tboard = deepcopy(board)
        move(d, tboard)
        dfs(tboard, depth+1)

dfs(board, 0)
print(answer)