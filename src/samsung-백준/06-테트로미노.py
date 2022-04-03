import sys; input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = max_num = -1
for b in board: max_num = max(max_num, max(b))

ds = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False]*M for _ in range(N)]
def dfs(r,c,depth,tot):
    global answer
    if depth == 4:
        if answer < tot: answer = tot
        return
    if answer > tot + max_num * (4-depth): return

    for d in ds:
        nr, nc = r + d[0], c + d[1]
        if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
        if visited[nr][nc]: continue
        if depth == 2:
            visited[nr][nc] = True
            dfs(r,c, depth+1, tot + board[nr][nc])
            visited[nr][nc] = False

        visited[nr][nc] = True
        dfs(nr,nc,depth+1,tot+board[nr][nc])
        visited[nr][nc] = False

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r,c,1,board[r][c])
        visited[r][c] = False

print(answer)