import sys; sys.stdin = open('d.txt', 'r')

N, K = map(int, input().split())

board = [[2]*(N+2)]
for _ in range(N):
    board.append([2] + list(map(int, input().split())) + [2])
board.append([2]*(N+2))

dirs = [(0,1),(0,-1),(-1,0),(1,0)]
flipd = [1,0,3,2]
poses = [ [[] for _ in range(N+2)] for _ in range(N+2) ]
horses = []

for i in range(K):
    r,c,d = map(int, input().split())
    d -= 1
    poses[r][c].append(i)
    horses.append((r,c,d))

def move_horse():
    end = False
    for h in range(K):
        r,c,d = horses[h]
        stacked = poses[r][c]
        idx = stacked.index(h)
        mvtarget = stacked[idx:]
        remains = stacked[:idx]
        
        nr = r + dirs[d][0]
        nc = c + dirs[d][1]
        # white
        if board[nr][nc] == 0:
            for t in mvtarget:
                _, _, td = horses[t]
                horses[t] = (nr,nc,td)
                
            poses[r][c] = remains
            poses[nr][nc].extend(mvtarget)
        # red
        elif board[nr][nc] == 1:
            for t in mvtarget:
                _, _, td = horses[t]
                horses[t] = (nr,nc,td)
            
            poses[r][c] = remains
            poses[nr][nc].extend(reversed(mvtarget))
        # blue
        elif board[nr][nc] == 2:
            nd = flipd[d]
            nr = r + dirs[nd][0]
            nc = c + dirs[nd][1]
            if board[nr][nc] == 2:
                horses[h] = (r,c,nd)
                continue
            
            for t in mvtarget:
                _, _, td = horses[t]
                horses[t] = (nr,nc,td)
            horses[h] = (nr,nc,nd)
            
            poses[r][c] = remains
            if board[nr][nc] == 1:
                poses[nr][nc].extend(reversed(mvtarget))
            else:
                poses[nr][nc].extend(mvtarget)
            
        if len(poses[nr][nc]) >= 4:
            end = True
            break
    return end

turn = 0
while True:
    turn += 1
    if turn > 1000: turn = -1; break
    if move_horse(): break

print(turn)