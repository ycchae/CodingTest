# N, M = map(int, input().split())
# board = [[0 for _ in range(M+1)] for _ in range(N+1)]
# answer = 0

# def dfs(count):
#     global answer
#     if count == N*M:
#         answer += 1
#         return
    
#     row = count // M +1
#     col = count % M +1

#     dfs(count +1)
#     if board[row-1][col] == 0 or board[row][col-1] == 0 or board[row-1][col-1] == 0:
#         board[row][col] = 1
#         dfs(count +1)
#         board[row][col] = 0

# dfs(0)
# print(answer)

N, M = map(int, input().split())
board = [[0 for _ in range(M+1)] for _ in range(N+1)]
answer = 0

def dfs(count):
    global answer
    if count == -1:
        answer += 1
        return
    
    row = count // M 
    col = count % M

    dfs(count -1)
    if board[row+1][col] == 0 or board[row][col+1] == 0 or board[row+1][col+1] == 0:
        board[row][col] = 1
        dfs(count -1)
        board[row][col] = 0

dfs(N * M-1)
print(answer)