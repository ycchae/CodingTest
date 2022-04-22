import sys; sys.stdin = open('../d.txt', 'r')

from collections import deque
import heapq

N, M, fuel = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

r, c = map(int, input().split())
taxi = (r-1,c-1)

guest = dict()
for _ in range(M):
    sr, sc, er, ec = map(lambda x: x-1, map(int, input().split()))
    guest[(sr,sc)] = (er,ec)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def find_guest():
    r,c = taxi
    if guest.get((r,c)):
        cand = [(r,c,0)]
    else:
        dq = deque([(r,c,0)])
        cand = []
        visited = [[False] * N for _ in range(N)]
        visited[r][c] = True

    if not cand:
        while dq:
            r,c, t = dq.popleft()
            if fuel <= t: break
            if cand and cand[0][2] <= t: continue

            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
                if visited[nr][nc]: continue
                if board[nr][nc]: visited[nr][nc] = True; continue

                visited[nr][nc] = True

                if guest.get((nr,nc)):
                    heapq.heappush(cand, (nr,nc,t+1))
                else:
                    dq.append((nr,nc,t+1))

    if not cand: return -1, -1, -1

    gr,gc,fspend = heapq.heappop(cand)
    return gr,gc,fspend


def go_target(guest_pos):
    r,c = guest_pos
    tr, tc = guest[guest_pos]
    if abs(tr-r) + abs(tc-c) > fuel:
        return -1

    dq = deque([(r, c, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True

    while dq:
        r,c,t = dq.popleft()

        if fuel < t: break
        if r == tr and c == tc:
            return t

        for d in dirs:
            nr = r + d[0]
            nc = c + d[1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if visited[nr][nc]: continue
            if board[nr][nc]: visited[nr][nc] = True; continue

            visited[nr][nc] = True
            dq.append((nr,nc, t+1))

    return -1

failed = False
for _ in range(M):
    gr, gc, fspend = find_guest()
    if gr == -1:
        failed = True
        break

    taxi = (gr,gc)
    fuel -= fspend

    if fuel <= 0:
        failed = True
        break

    fspend = go_target(taxi)
    if fspend < 0:
        failed = True
        break
    taxi = guest[(gr,gc)]
    del guest[(gr,gc)]
    fuel += fspend

if failed: print(-1)
else: print(fuel)