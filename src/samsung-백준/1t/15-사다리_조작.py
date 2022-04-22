import sys; sys.stdin = open('../d.txt', 'r')

N, M, H = map(int, input().split())
can = False

if M == 0: print(0); exit(0);

board = [[False]*N for _ in range(H)]
nline = [0]*(N)
for _ in range(M):
    a,b = map(int, input().split())
    board[a-1][b-1] = True
    nline[b-1] += 1


def check(bd):
    for n in range(N):
        c = n
        for r in range(H):
            if bd[r][c]:
                c += 1
            elif c-1 >= 0 and bd[r][c-1]:
                c -= 1
        if c != n:
            return False
    return True


def dfs(cur, r,c):
    global can
    if can: return
    if depth == cur:
        can = check(board)
        return

    odd = 0
    for j in nline:
        if j % 2 == 1:
            odd += 1
    if odd > 3 - cur:
        return


    for i in range(r, H):
        if i == r: k = c
        else: k = 0
        for j in range(k, N-1):
            if (j - 1 >= 0 and board[i][j - 1]) or board[i][j + 1] or board[i][j]: continue
            board[i][j] = True
            nline[j] += 1
            dfs(cur+1, i, j+2)
            board[i][j] = False
            nline[j] -= 1


for depth in range(5):
    if depth == 4: answer = -1; break
    dfs(0, 0,0)
    if can: answer = depth; break

print(answer)


# def check(pos):
#     for i in range(len(pos[0]) + 1):
#         pre = i
#         for j in range(len(pos)):
#             if i < len(pos[0]) and pos[j][i]:
#                 i += 1
#             elif i > 0 and pos[j][i - 1]:
#                 i -= 1
#         if pre != i:
#             return False
#     return True
#
#
# def dfs(pos, n, m, line):
#     if m <= n:
#         return m
#     if n == 4:
#         return 4
#     if check(pos):
#         return n
#     odd = 0
#     for i in line:
#         if i % 2 == 1:
#             odd += 1
#     if odd > 3 - n:
#         return 4
#     for i in range(len(pos)):
#         for j in range(len(pos[0])):
#             if pos[i][j]:
#                 continue
#             if j + 1 < len(pos[i]) and pos[i][j + 1]:
#                 continue
#             if j - 1 > 0 and pos[i][j - 1]:
#                 continue
#             pos[i][j] = True
#             line[j] += 1
#             m = min(m, dfs(pos, n + 1, m, line))
#             pos[i][j] = False
#             line[j] -= 1
#     return m
#
#
# n, m, p = map(int, input().split())
# pos = [[False for j in range(n - 1)] for i in range(p)]
# line = [0 for i in range(n - 1)]
#
# for i in range(m):
#     a = list(map(int, input().split()))
#     b = a[1] - 1
#     a = a[0] - 1
#     pos[a][b] = True
#     line[b] += 1
#
# answer = dfs(pos, 0, 4, line)
# if answer == 4:
#     answer = -1
#
# print(answer)