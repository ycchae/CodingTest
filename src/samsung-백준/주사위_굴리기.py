import sys; input = sys.stdin.readline
# right left north south
ds = [(0,1),(0,-1),(-1,0),(1,0)]

N, M, r,c, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
move = list(map(lambda x: x-1, map(int, input().split())))

dice = [[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]
# dtop = (1,1)
# dbot = (3,1)

for m in move:
    nr, nc = r + ds[m][0], c + ds[m][1]
    # print(nr, nc)    
    if nr < 0 or nc < 0 or nr >= N or nc >=M: continue
    

    if m < 2: # right left
        oleft = dice[1][0]
        omid = dice[1][1]
        oright = dice[1][2]
        obottom = dice[3][1]
        
        if m == 0: # right
            dice[1][0] = obottom
            dice[1][1] = oleft
            dice[1][2] = omid
            dice[3][1] = oright
        elif m == 1: # left
            dice[1][0] = omid
            dice[1][1] = oright
            dice[1][2] = obottom
            dice[3][1] = oleft
    else: # down up
        oback = dice[0][1]
        otop = dice[1][1]
        omid = dice[2][1]
        obot = dice[3][1]
        if m == 2:
            dice[0][1] = obot
            dice[1][1] = oback
            dice[2][1] = otop
            dice[3][1] = omid
        elif m == 3:
            dice[0][1] = otop
            dice[1][1] = omid
            dice[2][1] = obot
            dice[3][1] = oback

    print(dice[1][1])

    if board[nr][nc] == 0:
        board[nr][nc] = dice[3][1]
    else:
        dice[3][1] = board[nr][nc]
        board[nr][nc] = 0
    r, c = nr, nc
