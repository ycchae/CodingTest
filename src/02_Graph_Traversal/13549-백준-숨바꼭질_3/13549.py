X,Y = map(int, input().split())

max_pos = 100_000+1
from heapq import heappush, heappop
visited = [max_pos] * max_pos

def bfs():
    pq = []
    heappush(pq, (0, abs(X - Y), X))
    visited[X] = 0

    while pq:
        time, _, pos = heappop(pq)
        if pos == Y: return time

        for d in [-1, +1, 2]:
            new_time, new_pos = time+1, pos +d
            if d == 2: new_time, new_pos = time, pos *2
            if new_pos >= 0 and new_pos < max_pos and new_time < visited[new_pos] and new_pos < Y*2+1:
                heappush(pq, (new_time, abs(new_pos - Y), new_pos))
                visited[new_pos] = new_time

if Y < X: print(X-Y)
else: print(bfs())