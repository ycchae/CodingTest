import sys; sys.stdin = open('../d.txt', 'r')

answer = []
TC = int(input())

def top_move(r):
    tf = front[0][:]
    tbk = back[0][:]
    tl = left[0][:]
    tr = right[0][:]

    if r == '+':
        top[0][0], top[0][1], top[0][2], top[1][2], top[2][2], top[2][1], top[2][0], top[1][0] = \
        top[2][0], top[1][0], top[0][0], top[0][1], top[0][2], top[1][2], top[2][2], top[2][1]

        for i in range(3): left[0][i] = tf[i]
        for i in range(3): back[0][i] = tl[i]
        for i in range(3): right[0][i] = tbk[i]
        for i in range(3): front[0][i] = tr[i]
    elif r == '-':
        top[0][0], top[0][1], top[0][2], top[1][2], top[2][2], top[2][1], top[2][0], top[1][0] = \
        top[0][2], top[1][2], top[2][2], top[2][1], top[2][0], top[1][0], top[0][0], top[0][1]

        for i in range(3): left[0][i] = tbk[i]
        for i in range(3): front[0][i] = tl[i]
        for i in range(3): right[0][i] = tf[i]
        for i in range(3): back[0][i] = tr[i]

def bot_move(r):
    tf = front[2][:]
    tbk = back[2][:]
    tl = left[2][:]
    tr = right[2][:]

    if r == '+':
        bottom[0][0], bottom[0][1], bottom[0][2], bottom[1][2], bottom[2][2], bottom[2][1], bottom[2][0], bottom[1][0] = \
        bottom[2][0], bottom[1][0], bottom[0][0], bottom[0][1], bottom[0][2], bottom[1][2], bottom[2][2], bottom[2][1]

        for i in range(3): right[2][i] = tf[i]
        for i in range(3): back[2][i] = tr[i]
        for i in range(3): left[2][i] = tbk[i]
        for i in range(3): front[2][i] = tl[i]
    elif r == '-':
        bottom[0][0], bottom[0][1], bottom[0][2], bottom[1][2], bottom[2][2], bottom[2][1], bottom[2][0], bottom[1][0] = \
        bottom[0][2], bottom[1][2], bottom[2][2], bottom[2][1], bottom[2][0], bottom[1][0], bottom[0][0], bottom[0][1]

        for i in range(3): left[2][i] = tf[i]
        for i in range(3): back[2][i] = tl[i]
        for i in range(3): right[2][i] = tbk[i]
        for i in range(3): front[2][i] = tr[i]

def right_move(r):
    tt = [top[i][2] for i in range(3)]
    tbt = [bottom[i][2] for i in range(3)]
    tbk = [back[i][0] for i in range(3)]
    tf = [front[i][2] for i in range(3)]

    if r == '+':
        right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0] = \
        right[2][0], right[1][0], right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1]

        for i in range(3): top[i][2] = tf[i]
        for i in range(3): back[2-i][0] = tt[i]
        for i in range(3): bottom[2-i][2] = tbk[i]
        for i in range(3): front[i][2] = tbt[i]
    elif r == '-':
        right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0] = \
        right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0], right[0][0], right[0][1]

        for i in range(3): top[2-i][2] = tbk[i]
        for i in range(3): back[2-i][0] = tbt[i]
        for i in range(3): bottom[i][2] = tf[i]
        for i in range(3): front[i][2] = tt[i]

def left_move(r):
    tt = [top[i][0] for i in range(3)]
    tbt = [bottom[i][0] for i in range(3)]
    tbk = [back[i][2] for i in range(3)]
    tf = [front[i][0] for i in range(3)]

    if r == '+':
        left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0] = \
        left[2][0], left[1][0], left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1]

        for i in range(3): front[i][0] = tt[i]
        for i in range(3): bottom[i][0] = tf[i]
        for i in range(3): back[2-i][2] = tbt[i]
        for i in range(3): top[2-i][0] = tbk[i]
    elif r == '-':
        left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0] = \
        left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0], left[0][0], left[0][1]

        for i in range(3): back[2-i][2] = tt[i]
        for i in range(3): bottom[2-i][0] = tbk[i]
        for i in range(3): front[i][0] = tbt[i]
        for i in range(3): top[i][0] = tf[i]

def front_move(r):
    tt = top[2][:]
    tbt = bottom[0][:]
    tr = [right[i][0] for i in range(3)]
    tl = [left[i][2] for i in range(3)]

    if r == '+':
        front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0] = \
        front[2][0], front[1][0], front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1]

        for i in range(3): right[i][0] = tt[i]
        for i in range(3): bottom[0][2-i] = tr[i]
        for i in range(3): left[i][2] = tbt[i]
        for i in range(3): top[2][2-i] = tl[i]
    elif r == '-':
        front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0] = \
        front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0], front[0][0], front[0][1]

        for i in range(3): right[2-i][0] = tbt[i]
        for i in range(3): bottom[0][i] = tl[i]
        for i in range(3): left[2-i][2] = tt[i]
        for i in range(3): top[2][i] = tr[i]

def back_move(r):
    tt = top[0][:]
    tbt = bottom[2][:]
    tr = [right[i][2] for i in range(3)]
    tl = [left[i][0] for i in range(3)]

    if r == '+':
        back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0] = \
        back[2][0], back[1][0], back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1]

        for i in range(3): right[2-i][2] = tbt[i]
        for i in range(3): bottom[2][i] = tl[i]
        for i in range(3): left[2-i][0] = tt[i]
        for i in range(3): top[0][i] = tr[i]
    elif r == '-':
        back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0] = \
        back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0], back[0][0], back[0][1]

        for i in range(3): right[i][2] = tt[i]
        for i in range(3): bottom[2][2-i] = tr[i]
        for i in range(3): left[i][0] = tbt[i]
        for i in range(3): top[0][2-i] = tl[i]

for _ in range(TC):
    N = int(input())

    top = [['w'] * 3 for _ in range(3)] # 0
    bottom = [['y'] * 3 for _ in range(3)] # 1
    front = [['r'] * 3 for _ in range(3)] # 2
    back = [['o'] * 3 for _ in range(3)] # 3
    left = [['g'] * 3 for _ in range(3)] # 4
    right = [['b'] * 3 for _ in range(3)] # 5

    for dd in input().split():
        m, d = dd[0], dd[1]
        if m == 'U': top_move(d)
        elif m == 'D': bot_move(d)
        elif m == 'F': front_move(d)
        elif m == 'B': back_move(d)
        elif m == 'L': left_move(d)
        elif m == 'R': right_move(d)

    for t in top:
        answer.append(''.join(t))

print('\n'.join(answer))