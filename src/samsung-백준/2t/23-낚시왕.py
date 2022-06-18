import sys; sys.stdin = open('d.txt', 'r')

R,C,M = map(int, input().split())
board = dict()
remain = M

dirs = [(-1,0),(1,0),(0,1),(0,-1)]
cdirs = [1,0,3,2]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    d -= 1
    if d < 2:
        s = s % (R*2 - 2)
    else:
        s = s % (C*2 - 2)
    board[(r-1,c-1)] = (s,d,z)

answer = 0
for c in range(C):
    # person move and get
    for r in range(R):
        if board.get((r,c)):
            s,d,z = board[(r,c)]
            del board[(r,c)]
            answer += z
            remain -= 1
            break
    # shark move
    nboard = dict()
    keys = list(board.keys())
    for pos in keys:
        r,c = pos
        s,d,z = board[pos]
        del board[pos]
        nr, nc = r, c
        for _ in range(s):
            nr = nr + dirs[d][0]
            nc = nc + dirs[d][1]
            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                d = cdirs[d]
                nr = nr + dirs[d][0]*2
                nc = nc + dirs[d][1]*2
        
        if nboard.get((nr,nc)) is None:
            nboard[(nr,nc)] = [(s,d,z)]
        else:
            nboard[(nr,nc)].append((s,d,z))
        
    for pos, sharks in nboard.items():
        r,c = pos
        for shark in sharks:
            s,d,z = shark
            if not board.get(pos):
                board[pos] = (s,d,z)
            else:
                _,_,z1 = board[pos]
                if z1 < z:
                    board[pos] = (s,d,z)
                else:
                    remain -= 1
    
    if remain <= 0: break

print(answer)