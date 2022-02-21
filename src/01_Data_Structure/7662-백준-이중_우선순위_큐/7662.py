import sys
input = sys.stdin.readline
N = int(input())

import heapq
answer = []


for _ in range(N):
    M = int(input())

    visited = [False] * M
    maxheap = []
    minheap = []

    for i in range(M):
        op, x = input().split()
        x = int(x)

        if op == 'I':
            heapq.heappush(maxheap, (-x, i))
            heapq.heappush(minheap, (x, i))
            visited[i] = True
        else:
            if x == 1:
                while maxheap and visited[maxheap[0][1]] == False:
                    heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heapq.heappop(maxheap)
            else:
                while minheap and visited[minheap[0][1]] == False:
                    heapq.heappop(minheap)
                if minheap:
                    visited[minheap[0][1]] = False
                    heapq.heappop(minheap)

    if True not in visited:
        answer.append("EMPTY")
    else:
        while maxheap and visited[maxheap[0][1]] == False:
            heapq.heappop(maxheap)
        while minheap and visited[minheap[0][1]] == False:
            heapq.heappop(minheap)
        answer.append(f"{-maxheap[0][0]} {minheap[0][0]}")

print('\n'.join(answer))