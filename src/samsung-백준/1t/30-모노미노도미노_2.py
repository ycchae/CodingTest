import sys; sys.stdin = open('../d.txt', 'r')

GR, GC = 6, 4
BR, BC = 4, 6
gboard = [[0]*GC for _ in range(GR)]
bboard = [[0]*BC for _ in range(BR)]

def set_g_block(r,c,t):
    can = 0
    if t == 1:
        for i in range(GR):
            if gboard[i][c] == 0: can = i
            else: break
        gboard[can][c] = 1
    elif t == 2:
        for i in range(GR):
            if gboard[i][c] + gboard[i][c+1] == 0: can = i
            else: break
        gboard[can][c] = 1
        gboard[can][c + 1] = 1
    elif t == 3:
        for i in range(GR-1):
            if gboard[i][c] + gboard[i+1][c] == 0: can = i
            else: break
        gboard[can][c] = 1
        gboard[can+1][c] = 1

def set_b_block(r, c, t):
    can = 0
    if t == 1:
        for j in range(BC):
            if bboard[r][j] == 0: can = j
            else: break
        bboard[r][can] = 1
    elif t == 2:
        for j in range(BC-1):
            if bboard[r][j] + bboard[r][j+1] == 0: can = j
            else: break
        bboard[r][can] = 1
        bboard[r][can+1] = 1
    elif t == 3:
        for j in range(BC):
            if bboard[r][j] + bboard[r+1][j] == 0: can = j
            else: break
        bboard[r][can] = 1
        bboard[r+1][can] = 1

def del_gboard():
    dline = []
    for i in range(GR-1, 2-1, -1):
        if any(gboard[i][j] == 0 for j in range(GC)): continue
        dline.append(i)
    return dline

def del_bboard():
    dline = []
    for j in range(BC-1, 2-1, -1):
        if any(bboard[i][j] == 0 for i in range(BR)): continue
        dline.append(j)
    return dline

def move_gboard(dline, cleantop=[]):
    for e, d in enumerate(dline):
        for i in range(d + e, 0 + e, -1):
            for j in range(GC):
                gboard[i][j] = gboard[i-1][j]


    for t in cleantop:
        gboard[t] = [0]*GC

def move_bboard(dline, cleantop=[]):
    for e, d in enumerate(dline):
        for j in range(d+e, 0+e, -1):
            for i in range(BR):
                bboard[i][j] = bboard[i][j-1]

    for t in cleantop:
        for i in range(BR):
            bboard[i][t] = 0

def over_gboard():
    mv = []
    clean = []
    cnt = 0
    for i in range(2):
        if any(gboard[i][j] for j in range(GC)):
            mv.append(5-cnt)
            cnt += 1
            clean.append(i)

    move_gboard(mv, cleantop=clean)

def over_bboard():
    mv = []
    clean = []
    cnt = 0
    for j in range(2):
        if any(bboard[i][j] for i in range(BR)):
            mv.append(5-cnt)
            cnt += 1
            clean.append(j)

    move_bboard(mv, cleantop=clean)

score = 0
N = int(input())
for _ in range(N):
    t, r, c = map(int, input().split())
    set_g_block(r,c,t)
    set_b_block(r,c,t)

    dline = del_gboard()
    if dline:
        score += len(dline)
        move_gboard(dline)

    dline = del_bboard()
    if dline:
        score += len(dline)
        move_bboard(dline)

    over_gboard()
    over_bboard()

print(score)
bcnt, gcnt = 0, 0
for i in range(BR): bcnt += bboard[i].count(0)
for i in range(GR): gcnt += gboard[i].count(0)

print(BR*BC + GR*GC - gcnt - bcnt)