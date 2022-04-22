import sys; sys.stdin = open('d.txt', 'r')

N = int(input())
board = []
fish = [0]*7
for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(N):
        if 0 < line[j] <= 6:
            fish[line[j]] += 1
        elif line[j] == 9:
            shark = (i,j)
            board[i][j] = 0

size = 2
dirs = [(-1,0),(1,0),(0,1),(0,-1)]

def eat():
    global shark

    r,c = shark
    visited = [[N*N] * N for _ in range(N)]

    visited[r][c] = 0
    q = [(r,c,0)]
    candidates = []
    min_dist = N*N
    while q:
        r,c,dist = q.pop()
        if min_dist < dist+1: continue
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visited[nr][nc] <= dist+1: continue
            if board[nr][nc] > size: continue
            visited[nr][nc] = dist+1
            q.append((nr,nc, dist+1))
            if 0 < board[nr][nc] < size:
                if dist + 1 < min_dist:
                    min_dist = dist + 1
                    candidates = []
                candidates.append( ((nr,nc), board[nr][nc]) )

    if candidates:
        candidates.sort(key = lambda x: x[0])
        p, s = candidates[0]
        r,c = p
        board[r][c] = 0
        fish[s] -= 1

        shark = (r,c)
        return min_dist

    return 0


time = 0
cnt = 0
while sum(fish[:size+1]):
    res = eat()
    if not res: break
    time += res

    if size < 7:
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1

print(time)


