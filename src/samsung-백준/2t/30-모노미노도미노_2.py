import sys; sys.stdin = open('d.txt','r')

N = int(input())

GC, GR = 4, 6
BC, BR = 6, 4
green = [[0]*4 for _ in range(6)]
blue = [[0]*6 for _ in range(4)]
        
def org_green(base):
    for c in range(GC):
        for r in range(base, 0, -1):
            green[r][c] = green[r-1][c]
    green[0] = [0] * GC
    
def org_blue(base):
    for r in range(4):
        for c in range(base, 0, -1):            
                blue[r][c] = blue[r][c-1]
    for i in range(BR): blue[i][0] = 0

def set_green(t,tr,tc):
    can = -1
    if t == 1:
        for r in range(6):
            if green[r][tc] > 0: break
            can = r
        green[can][tc] = 1

    elif t == 2:
        for r in range(6):
            if green[r][tc] > 0 or green[r][tc+1] > 0: break
            can = r
        green[can][tc] = 1
        green[can][tc+1] = 1
        
    elif t == 3:
        for r in range(5):
            if green[r][tc] > 0 or green[r+1][tc] > 0: break
            can = r
        green[can][tc] = 1
        green[can+1][tc] = 1

def set_blue(t,tr,tc):
    can = -1
    if t == 1:
        for c in range(6):
            if blue[tr][c] > 0: break
            can = c
        blue[tr][can] = 1

    elif t == 2:
        for c in range(5):
            if blue[tr][c] > 0 or blue[tr][c+1] > 0: break
            can = c
        blue[tr][can] = 1
        blue[tr][can+1] = 1
        
    elif t == 3:
        for c in range(6):
            if blue[tr][c] > 0 or blue[tr+1][c] > 0: break
            can = c
        blue[tr][can] = 1
        blue[tr+1][can] = 1
        

def check_green():
    bases = []
    for i in range(2, 6):
        if sum(green[i]) == 4:
            bases.append(i)
    for b in bases:
        org_green(b)
    return len(bases)    


def check_blue():
    bases = []
    for j in range(2, 6):
        if all(blue[i][j] == 1 for i in range(4)):
            bases.append(j)
    for b in bases:
        org_blue(b)
    return len(bases)


def trunc_green():
    cnt = 0
    for i in range(2):
        if any(green[i][j] == 1 for j in range(4)):
            cnt += 1

    for _ in range(cnt):
        org_green(GR-1)
    
def trunc_blue():
    cnt = 0
    for j in range(2):
        if any(blue[i][j] == 1 for i in range(4)):
            cnt += 1
    for _ in range(cnt):
        org_blue(BC-1)
    
score = 0
for _ in range(N):
    t, tr, tc = map(int, input().split())
    set_green(t, tr, tc)
    set_blue(t, tr, tc)
    
    score += check_green()
    score += check_blue()
        
    trunc_green()
    trunc_blue()

num = 0
for g in green:
    num += sum(g)
for b in blue:
    num += sum(b)

print(score)
print(num)