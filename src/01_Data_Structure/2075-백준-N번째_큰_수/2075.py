import sys
input = sys.stdin.readline

N = int(input())
capacity = N

import heapq

heap = []
for _ in range(N):
    arr = list(map(int, input().split()))
    for i in range(N):
        if len(heap) < capacity:
            heapq.heappush(heap, arr[i])
        elif heap[0] < arr[i]:
            heapq.heappushpop(heap, arr[i])

print(heap[0])