import sys; input=sys.stdin.readline
N = int(input())
board = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    board.append((x,a))
    people += a
board.sort(key=lambda x: x[0])

cnt = 0
for x, a in board:
    cnt += a
    if cnt > people/2:
        print(x)
        break