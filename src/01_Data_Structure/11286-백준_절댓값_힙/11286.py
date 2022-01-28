import sys
input = sys.stdin.readline
N = int(input())

import heapq
heap = []

answer = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            answer.append(heapq.heappop(heap)[1])
        else:
            answer.append(0)
    else:
        heapq.heappush(heap, ((abs(x), x), x))

print('\n'.join(map(str, answer)))