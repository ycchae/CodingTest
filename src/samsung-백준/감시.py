import sys;
sys.stdin = open('d.txt', 'r')

N, M = map(int, input().split())
board = []
cctv = []
nwall = 0
ncam = 0
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        cam = board[i][j]
        if cam == 6:
            nwall += 1
        elif cam != 0:
            cctv.append([cam,i,j])
            ncam += 1
directions = [(-1,0), (0,1), (1,0), (0,-1)]
cams = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[3,0,1],[2,3,0],[1,2,3]],
    [[0,1,2,3]]
]

minval = int(1e9)
if ncam == 0:
    print(N*M - nwall)
    exit()

def copy(bb):
    t = []
    for b in bb:
        t.append(b[:])
    return t
def see(bd, r,c,mm):
    for d in mm:
        nr, nc = r, c
        while True:
            nr += directions[d][0]
            nc += directions[d][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: break
            if bd[nr][nc] == 6: break
            if bd[nr][nc] == 0: bd[nr][nc] = 7

def dfs(on, b):
    global minval
    if on == ncam:
        val = 0
        for i in range(N):
            val += b[i].count(0)
        if minval > val: minval = val
        return

    cam, r, c = cctv[on]
    for mm in cams[cam]:
        temp = copy(b)
        see(temp, r,c, mm)
        dfs(on+1, temp)

dfs(0, board)
print(minval)