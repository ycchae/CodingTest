import sys; sys.stdin = open('../d.txt', 'r')

dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

N, M, K = map(int, input().split())

fireballs = []
board = [ [[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fireballs.append([r,c,m,s,d])

def move():
    while fireballs:
        r,c,m,s,d = fireballs.pop()
        nr = (r + dirs[d][0] * s) % N
        nc = (c + dirs[d][1] * s) % N
        board[nr][nc].append([m,s,d])

def divide():
    for i in range(N):
        for j in range(N):
            lb = len(board[i][j])
            if lb == 1:
                fireballs.append([i,j] + board[i][j].pop())
            elif lb > 1:
                nm, ns = 0, 0
                odd, even = 0, 0
                while board[i][j]:
                    m,s,d = board[i][j].pop()
                    nm += m
                    ns += s
                    if d % 2 == 0: even += 1
                    else: odd += 1

                nm = nm // 5
                if nm <= 0: continue

                ns = ns // lb
                if even == lb or odd == lb:
                    nd = [0,2,4,6]
                else:
                    nd = [1,3,5,7]

                for d in nd:
                    fireballs.append([i,j,nm,ns,d])

for _ in range(K):
    move()
    divide()

answer = 0
for fb in fireballs:
    answer += fb[2]

print(answer)