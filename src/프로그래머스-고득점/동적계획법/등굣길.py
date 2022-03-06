answer_division = 1_000_000_007
def solution(m, n, puddles):
    board = [[0] * (m+1) for _ in range(n+1)]
    board[1][1] = 1
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == 1 and c == 1: continue
            if [c, r] in puddles: continue
            board[r][c] = (board[r][c-1] + board[r-1][c]) % answer_division
    return board[n][m]

print(solution(4,3,[[2,2]]))