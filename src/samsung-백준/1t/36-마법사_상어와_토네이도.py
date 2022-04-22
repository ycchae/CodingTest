import sys; sys.stdin = open('../d.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

answer = 0

def handle_blow():
    global answer
    for dust, poses in blow.items():
        for pos in poses:
            r,c = pos
            if r < 0 or c < 0 or r >= N or c >= N:
                answer += dust
            else:
                board[r][c] += dust


pos = [(N//2, N//2, 6)]
cnt = 0
criteria = 1
end = False
while pos:
    for crt in range(criteria):
        xr,xc,d = pos.pop()
        yr, yc = xr + dirs[d][0], xc + dirs[d][1]
        if yr < 0 or yc < 0: end = True; break
        if crt + 1 != criteria:
            pos.append((yr, yc, d))

        ydust = board[yr][yc]
        if ydust > 0: blow = dict()
        else: continue

        alpha = ydust
        board[yr][yc] = 0
        for percent in [10,7,5,2,1]:
            dust = int(ydust * (percent / 100))
            if dust <= 0: break
            if not blow.get(dust): blow[dust] = []
            if percent == 10:
                blow[dust].extend([(yr + dirs[(d+1) % 8][0], yc + dirs[(d+1) % 8][1]), (yr + dirs[(d-1) % 8][0], yc + dirs[(d-1) % 8][1])])
                alpha -= dust * 2
            elif percent == 7:
                blow[dust].extend([(yr + dirs[(d+2) % 8][0], yc + dirs[(d+2) % 8][1]), (yr + dirs[(d-2) % 8][0], yc + dirs[(d-2) % 8][1])])
                alpha -= dust * 2
            elif percent == 2:
                blow[dust].extend([(yr + dirs[(d+2) % 8][0]*2, yc + dirs[(d+2) % 8][1]*2), (yr + dirs[(d-2) % 8][0]*2, yc + dirs[(d-2) % 8][1]*2)])
                alpha -= dust * 2
            elif percent == 1:
                blow[dust].extend([(yr + dirs[(d+3) % 8][0], yc + dirs[(d+3) % 8][1]), (yr + dirs[(d-3) % 8][0], yc + dirs[(d-3) % 8][1])])
                alpha -= dust * 2
            elif percent == 5:
                blow[dust].extend([(yr + dirs[d][0]*2, yc + dirs[d][1]*2)])
                alpha -= dust

        if not blow.get(alpha):
            blow[alpha] = []
        blow[alpha].extend([(yr + dirs[d][0], yc + dirs[d][1])])

        handle_blow()

    if end: break
    cnt += 1
    if cnt % 2 == 0:
        criteria += 1

    nd = (d - 2) % 8

    pos.append((yr,yc,nd))

print(answer)