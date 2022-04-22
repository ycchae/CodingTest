import sys; sys.stdin = open('../d.txt', 'r')

N, Q = map(int, input().split())
size = 2**N
board = [list(map(int, input().split())) for _ in range(size)]
answer_ice = 0
answer_sum = 0

for b in board:
    answer_sum += sum(b)

def move(L):
    if not L: return
    lsize = 2**L
    for r in range(size // lsize):
        r = r * lsize
        for c in range(size // lsize):
            c = c * lsize

            tmpb = []
            for i in range(lsize):
                tmpb.append(board[r + i][c:c+lsize])

            for i in range(lsize):
                for j in range(lsize):
                    board[r + j][c + lsize -1 -i] = tmpb[i][j]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def remove():
    global answer_sum

    del_cand = []
    for i in range(size):
        for j in range(size):
            if not board[i][j]: continue

            if (i,j) == (0,0) or (i,j) == (0,size-1) or (i,j) == (size-1, 0) or (i,j) == (size-1, size-1):
                del_cand.append((i,j))
                continue

            cnt = 0
            for di, d in enumerate(dirs):
                if cnt >= 3: break
                if cnt + (4 - di) < 3: break
                ni = i + d[0]
                nj = j + d[1]
                if ni < 0 or nj < 0 or ni >= size or nj >= size: continue
                if board[ni][nj]:
                    cnt += 1

            if cnt < 3:
                del_cand.append((i, j))

    for pos in del_cand:
        r,c = pos
        board[r][c] -= 1
        answer_sum -= 1


for L in map(int, input().split()):
    move(L)
    remove()

visited = [[False] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        if board[i][j] and not visited[i][j]:
            visited[i][j] = True
            q = [(i,j)]
            cnt = 1
            while q:
                r,c = q.pop()
                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < 0 or nc < 0 or nr >= size or nc >= size: continue
                    if visited[nr][nc]: continue
                    if not board[nr][nc]: continue
                    visited[nr][nc] = True
                    cnt += 1
                    q.append((nr,nc))

            if cnt == 1: continue
            if cnt > answer_ice:
                answer_ice = cnt

print(answer_sum)
print(answer_ice)