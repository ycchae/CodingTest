import sys
input = sys.stdin.readline

N = int(input())
tmp = list(map(int, input().split()))

moves = []
for i in range(N) :
    moves.append((tmp[i], i+1))

index = 0
answer = []
while True:
    move = moves[index][0]
    answer.append(moves[index][1])
    moves.pop(index)
    len_moves = len(moves)
    if len_moves == 0:
        break
    if move > 0:
        index = (index + move -1) % len_moves
    else:
        index = (index + move) % len_moves

print(' '.join(map(str, answer)))