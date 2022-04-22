import sys; sys.stdin = open('../d.txt', 'r')

R,C,M = map(int, input().split())

sharks = dict()
for i in range(M):
    r,c,s,d,z = map(int, input().split())
    if d-1 < 2: s = s % ((R-1)*2)
    else: s = s % ((C-1)*2)
    sharks[(r-1, c-1)] = (s,d-1,z)

flip = [1,0,3,2]
dirs = [(-1,0),(1,0),(0,1),(0,-1)]
def shark_move(pos, val):
    r,c = pos
    s,d,z = val

    if s == 0: return (r,c), (s,d,z)

    nr, nc = r + s*dirs[d][0], c + s*dirs[d][1]
    if 0 <= nr < R and 0 <= nc < C:
        return (nr, nc), val

    ns = s
    if d == 0: ns += (R-1) - r
    elif d == 1: ns += r
    elif d == 2: ns += c
    elif d == 3: ns += (C-1)-c

    if d < 2:
        k = (ns - 1) // (R - 1)
        go = ns - k * (R - 1)
    else:
        k = (ns - 1) // (C - 1)
        go = ns - k * (C - 1)

    if k % 2 == 1:
        d = flip[d]

    if d == 0: nr, nc = R-1, c
    elif d == 1: nr, nc = 0, c
    elif d == 2: nr, nc = r, 0
    elif d == 3: nr, nc = r, C-1

    nr += dirs[d][0] * go
    nc += dirs[d][1] * go

    return (nr, nc), (s, d, z)

answer = 0
sharks_num = M
for j in range(C):
    if sharks_num == 0: break
    for i in range(R):
        if sharks.get((i,j)):
            answer += sharks[(i, j)][2]
            sharks_num -= 1
            del sharks[(i, j)]
            break

    nsharks = dict()
    for pos, vals in sharks.items():
        npos, nvals = shark_move(pos, vals)
        if not nsharks.get(npos):
            nsharks[npos] = nvals
        else:
            if nsharks[npos][2] < nvals[2]:
                nsharks[npos] = nvals
            sharks_num -= 1
    sharks = nsharks
print(answer)