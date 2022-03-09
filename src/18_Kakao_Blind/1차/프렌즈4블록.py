from collections import defaultdict
def solution(m, n, board):
    answer = 0
    empty = "-1"
    for i in range(m): board[i] = list(board[i])
    
    directions = [(1,0),(0,1),(1,1)]
    delset = defaultdict(set)

    while True:
        delcount = 0

        # check
        for r in range(m-1):
            for c in range(n-1):
                if board[r][c] == empty: continue
                #  check4
                checked = True
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if nr < 0 or nc < 0 or nr >= m or nc >= n: checked = False; break
                    if board[nr][nc] != board[r][c]: checked = False; break
                if checked: delset[board[r][c]].update([(r,c),(r+1,c),(r,c+1),(r+1,c+1)])
        # del
        for k, v in delset.items():
            delcount += len(v)
            for r,c in v: board[r][c] = empty
            delset[k] = set()

        if delcount == 0: return answer
        answer += delcount

        # down
        for c in range(n):
            stack = []
            for r in range(m):
                if board[r][c] != empty: stack.append(board[r][c])

            for r in range(m-1,-1,-1):
                if stack: board[r][c] = stack.pop()
                else: board[r][c] = empty


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(2,2,["CC", "CC"]))