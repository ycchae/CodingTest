import sys; sys.stdin = open('d.txt', 'r')

def solution():
    global answer
    board = dict()
    for i in range(20):
        board[i] = [(i+1, (i+1)*2)]
    board[20] = [(21, 0)]
    END = 21
    board[5].append((23, 13))
    board[23] = [(24, 16)]
    board[24] = [(25, 19)]
    board[25] = [(26, 25)]
    board[26] = [(27, 30)]
    board[27] = [(28, 35)]
    board[28] = [(20, 40)]
    
    board[10].append((29,22))
    board[29] = [(30,24)]
    board[30] = [(26,25)]
    
    board[15].append((31,28))
    board[31] = [(32, 27)]
    board[32] = [(33, 26)]
    board[33] = [(26, 25)]

    speed = list(map(int, input().split()))
    
    def go(cur, s):
        for ss in range(s):
            if cur == END:
                return END, 0
            if ss == 0: p = -1
            else: p = 0
            nxt, score = board[cur][p]
            cur = nxt
        return cur, score
    
    pos = [0]*4
    def dfs(score, depth, dead):
        global answer
        if score + (10-depth)*40 <= answer: return
        if depth >= 10 or dead == 4:
            if answer < score:
                answer = score
            return
            
        for i in range(4):
            p = pos[i]
            if p == END: continue
            ncur, sc = go(p, speed[depth])
            if ncur != END:
                if ncur in pos: continue
            
            score += sc
            pos[i] = ncur
            if ncur == END:
                dead += 1

            dfs(score, depth+1, dead)
            
            score -= sc
            pos[i] = p
            if ncur == END:
                dead -= 1
            
    dfs(0, 0, 0)
    return answer
    

for a in [190,133,214,130]:
    answer = 0
    s = solution()
    print(s, s == a)