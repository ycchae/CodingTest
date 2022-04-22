N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def check(line):
    height = line[0]
    visited = [False] * N
    i = 1
    while i < N:
        if line[i] == height: i += 1; continue
        # 높이 다르면 높이 1차이 나야함
        if abs(height - line[i]) != 1: return False

        # 높 -> 낮
        if height - line[i] == 1:
            if not (i + L <= N and all(not visited[j] and line[j] == line[i] for j in range(i, i + L))): return False
            height = line[i]
            for j in range(i, i+L): visited[j] = True
            i = i + L
        # 낮 -> 높
        elif height - line[i] == -1:
            if not (0 <= i-L and all(not visited[j] and line[j] == height for j in range(i-1, i-L-1, -1))): return False
            height = line[i]
            for j in range(i-1, i-1-L, -1): visited[j] = True
            i += 1
    return True

answer = 0
for i in range(N):
    if check(board[i]): answer += 1

for j in range(N):
    line = []
    for i in range(N):
        line.append(board[i][j])
    if check(line): answer += 1

print(answer)
