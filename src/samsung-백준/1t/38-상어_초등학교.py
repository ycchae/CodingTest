N = int(input())

like = dict()
for _ in range(N*N):
    stn, l1,l2,l3,l4 = map(int, input().split())
    like[stn] = [l1,l2,l3,l4]

board = [[0]*N for _ in range(N)]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
for i, stn in enumerate(like.keys()):
    if i == 0:
        board[1][1] = stn
        continue
    likef = like[stn]

    cand = []
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0: continue
            like_score = 0
            empty = 0
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
                if board[nr][nc] > 0:
                    for f in range(4):
                        if board[nr][nc] == likef[f]:
                            like_score -= 1
                            break
                else:
                    empty -= 1

            cand.append((like_score, empty, r, c))

    cand.sort()

    _, _, r, c = cand[0]
    board[r][c] = stn

answer = 0
score = [0,1,10,100,1000]
for r in range(N):
    for c in range(N):
        stn = board[r][c]
        likef = like[stn]
        like_score = 0
        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            for f in range(4):
                if board[nr][nc] == likef[f]:
                    like_score += 1

        answer += score[like_score]

print(answer)