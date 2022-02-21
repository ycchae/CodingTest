import sys; input=sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
def dc(r,c,n):
    if n == 2: return sorted([board[r][c], board[r][c+1], board[r+1][c], board[r+1][c+1]])[-2]
    n00, n01 = dc(r, c, n//2), dc(r, c+n//2, n//2)
    n10, n11 = dc(r+n//2, c, n//2), dc(r+n//2, c+n//2, n//2)
    return sorted([n00, n01, n10, n11])[-2]
print(dc(0,0,N))