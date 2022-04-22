import sys; input =sys.stdin.readline
answer = sys.maxsize
N, M = map(int, input().split())
# down, up, right, left
directions = [(1,0),(-1,0),(0,1),(0,-1)]

init_red,init_blue,hole = 0,0,0
board = []
for i in range(N):
    board.append([])
    b = list(input())
    for j in range(M):
        if b[j] == 'R': init_red = (i,j)
        elif b[j] == 'B': init_blue = (i,j)
        elif b[j] == 'O': hole = (i,j)
        board[i].append(b[j])

answer = -1
def dfs(red, blue, depth, prev):
    global answer

    if depth > 10: return
    if red == hole:
        if answer == -1 or answer > depth: answer = depth
        return
    if answer != -1 and depth + 1 >= answer: return

    for i, d in enumerate(directions):
        if i == prev: continue
        if i == 0 and prev == 1: continue
        if i == 1 and prev == 0: continue
        if i == 2 and prev == 3: continue
        if i == 3 and prev == 2: continue
        r = max(red[0],blue[0])
        c = max(red[1],blue[1])
        if i == 0:    
            if r == red[0]: first = red; second = blue
            else: first = blue; second = red
        elif i == 1:
            if r == red[0]: first = blue; second = red
            else: first = red; second = blue
        elif i == 2:
            if c == red[1]: first = red; second = blue
            else: first = blue; second = red
        elif i == 3:
            if c == red[1]: first = blue; second = red
            else: first = red; second = blue
        
        first_hole, second_hole = False, False

        move = 0
        nr, nc = first[0] + move * d[0], first[1] + move * d[1]
        while board[nr][nc] != '#' and (nr,nc) != second:
            move += 1
            nr, nc = first[0] + move * d[0], first[1] + move * d[1]
            if (nr, nc) == hole: first_hole = True; break
        move -= 1
        if first == red:
            if first_hole: nred = hole
            else: nred = (first[0] + move * d[0], first[1] + move * d[1])
        else: 
            if first_hole: nblue = hole
            else: nblue = (first[0] + move * d[0], first[1] + move * d[1])

        if first_hole: first = (-1,-1)
        else: first = (first[0] + move * d[0], first[1] + move * d[1])

        move = 0
        nr, nc = second[0] + move * d[0], second[1] + move * d[1]
        while board[nr][nc] != '#' and (nr,nc) != first:
            move += 1
            nr, nc = second[0] + move * d[0], second[1] + move * d[1]
            if (nr, nc) == hole: second_hole = True; break
        move -= 1
        if second == red:
            if second_hole: nred = hole
            else: nred = (second[0] + move * d[0], second[1] + move * d[1])
        else:
            if second_hole: nblue = hole
            else: nblue = (second[0] + move * d[0], second[1] + move * d[1])

        if red == nred and blue == nblue: continue
        if nblue == hole: continue
        dfs(nred, nblue, depth+1, i)

dfs(init_red, init_blue, 0, -1)
print(answer)