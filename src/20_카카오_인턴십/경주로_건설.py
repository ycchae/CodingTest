from collections import deque
def solution(board):
    N = len(board)

    straight, corner = 1, 5
    maximum = (corner+straight)*N*N
    directions = [(1,0,1),(-1,0,2),(0,1,3),(0,-1,4)]
    visited = [[maximum]*N for _ in range(N)]    
    visited[0][0] = 0
    
    dq = deque([])
    if board[1][0] != 1:
        dq.append((1,0,straight,1))
        visited[1][0] = straight
    if board[0][1] != 1:
        dq.append((0,1,straight,3))
        visited[0][1] = straight

    answer = maximum
    while dq:
        r, c, cost, d = dq.popleft()
        if r == N-1 and c == N-1:
            if answer > cost: answer = cost
            continue

        for direction in directions:
            nr = r + direction[0]
            nc = c + direction[1]
            if nr == 0 and nc == 0: continue

            nd = direction[2]
            if (d == 1 and nd == 2) or (d == 3 and nd == 4): continue
            if nd != d: ncost = cost + corner + straight
            else: ncost = cost + straight

            if nr < 0 or nc < 0 or nr >=N or nc >= N: continue
            if board[nr][nc]: continue
            if visited[nr][nc] < ncost - (corner-straight): continue

            visited[nr][nc] = ncost
            dq.append((nr,nc,ncost,nd))

    return answer*100

# print(solution([[0,0,1],[1,0,0],[1,1,0]]))
# print(solution([[0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,0],[1,0,0,1,0,0,0,0],[1,1,0,0,0,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,0]]))

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))