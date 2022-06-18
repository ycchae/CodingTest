import sys; sys.stdin = open('d.txt', 'r')

R, C = 3, 3
r,c,k = map(int, input().split())
r -= 1
c -= 1
board = dict()
for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if not board.get(i):
            board[i] = dict()
        board[i][j] = line[j]
        
def cs(ct):
    res = []
    for i, v in ct.items():
        res.append((v,i))
    res.sort()
    return res


def rop():
    global C
    maxC = 0
    for i in range(R):
        ct = dict()
        for j in range(C):
            if board.get(i) and board[i].get(j) and board[i][j] > 0:
                if not ct.get(board[i][j]):
                    ct[board[i][j]] = 0
                ct[board[i][j]] += 1
        
        res = cs(ct)
        j = 0
        board[i] = dict()
        for v, n in res:
            board[i][j] = n
            board[i][j+1] = v
            j += 2
            if j >= 100: break
        if j > maxC: maxC = j
    C = maxC


def cop():
    global R
    maxR = 0
    for j in range(C):
        ct = dict()
        for i in range(R):
            if board.get(i) and board[i].get(j) and board[i][j] > 0:
                if not ct.get(board[i][j]):
                    ct[board[i][j]] = 0
                ct[board[i][j]] += 1

        res = cs(ct)
        i = 0
        for v, n in res:
            if not board.get(i):
                board[i] = dict()
            if not board.get(i+1):
                board[i+1] = dict()
            board[i][j] = n
            board[i+1][j] = v
            i += 2
            if i >= 100: break
        
        for ii in range(i, R):
            board[ii][j] = 0
        if i > maxR: maxR = i
    R = maxR
            

sec = 0
while True:
    if board.get(r) and board[r].get(c) == k:
        break
    
    if R >= C: rop(); op = 'R'
    else: cop(); op = 'C'
    
    sec += 1
    if sec == 101:
        sec = -1
        break
    
print(sec)