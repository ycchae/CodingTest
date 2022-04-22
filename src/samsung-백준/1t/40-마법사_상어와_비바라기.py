import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1

    cant = dict()
    for cloud in clouds:
        r, c = cloud
        nr = (r + dirs[d][0] * s) % N
        nc = (c + dirs[d][1] * s) % N
        board[nr][nc] += 1
        cant[(nr,nc)] = True

    for update in cant:
        r, c = update
        cnt = 0
        for d in [1,3,5,7]:
            nr = r + dirs[d][0]
            nc = c + dirs[d][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if board[nr][nc] >= 1:
                cnt += 1
        board[r][c] += cnt


    new_clouds = []
    for i in range(N):
        for j in range(N):
            if cant.get((i,j)): continue
            if board[i][j] >= 2:
                board[i][j] -= 2
                new_clouds.append((i,j))
    clouds = new_clouds

answer = 0
for b in board:
    answer += sum(b)
print(answer)