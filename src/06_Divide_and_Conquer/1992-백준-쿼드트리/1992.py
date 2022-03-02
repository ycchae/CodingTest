import sys
input = sys.stdin.readline

N = int(input())
strs = [input().strip() for _ in range(N)]
board = []
for i in range(N):
    board.append([])
    for j in range(N):
        board[i].append(int(strs[i][j]))

answer = []
def dc(r,c,n):
    if all(board[i][j] == 0 for i in range(r, r+n) for j in range(c, c+n)):
        answer.append('0')
        return 
    if all(board[i][j] == 1 for i in range(r, r+n) for j in range(c, c+n)):
        answer.append('1')
        return 
    if not all(board[i][j] == 0 for i in range(r, r + n//2) for j in range(c, c + n//2)) or \
        not all(board[i][j] == 1 for i in range(r, r + n//2) for j in range(c, c + n//2)):
        answer.append('(')
        dc(r,c,n//2)
        dc(r,c+n//2,n//2)
        dc(r+n//2,c,n//2)
        dc(r+n//2,c+n//2,n//2)
        answer.append(')')
        return ''

dc(0,0,N)
print(''.join(answer))