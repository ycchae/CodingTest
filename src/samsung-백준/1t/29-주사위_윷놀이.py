import sys; sys.stdin = open('../d.txt', 'r')

route0 = list(range(0,41,2))
route10 = [13,16,19]
route20 = [22,24]
route30 = [28,27,26]
route25 = [25,30,35]

route = [route0, route10, route20, route30, route25]

arrive = (5,0)
pos = [(0,0)] * 4
move = list(map(int, input().split()))

def get_npos(r,c, m):
    if r == 0 and route[r][c] == 10:
        r = 1
        c = 0
        m -= 1
    elif r == 0 and route[r][c] == 20:
        r = 2
        c = 0
        m -= 1
    elif r == 0 and route[r][c] == 30:
        r = 3
        c = 0
        m -= 1

    if m > 0:
        if 0 < r < 4 and len(route[r]) <= c + m:
            m -= len(route[r]) - c
            r = 4
            c = 0
        if m > 0:
            if len(route[r]) <= c + m:
                if r == 4:
                    if c+m == len(route[r]):
                        r = 0
                        c = len(route[r])-1
                        return (r,c)
                    else:
                        return (5,0)
                elif r == 0:
                    return (5, 0)
                else:
                    print('error!', r,c)

    return (r, c+m)

answer = 0
def dfs(score, depth):
    global answer
    if score + ((10 - depth) * 40) < answer:
        return

    if depth == 10:
        if score > answer: answer = score;
        return

    for i in range(4):
        cur = pos[i]
        if cur == arrive: continue

        r,c = cur
        npos = get_npos(r,c, move[depth])
        nr,nc = npos
        if nr < arrive[0] and npos in pos: continue

        pos[i] = npos
        if npos == arrive:
            dfs(score + 0, depth + 1)
        else:
            dfs(score + route[nr][nc], depth + 1)
        pos[i] = cur

dfs(0, 0)

print(answer)