import sys; input=sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0
def dc(r,c,n):
    global blue
    global white
    color = board[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != board[i][j]:
                dc(r, c, n//2)
                dc(r, c+n//2, n//2)
                dc(r+n//2, c, n//2)
                dc(r+n//2, c+n//2, n//2)
                return
    if color == 1: blue += 1
    else: white += 1
    
dc(0,0,N)
print(white)
print(blue)