import sys
input = sys.stdin.readline

N = int(input())

from queue import PriorityQueue
q = PriorityQueue()

answer = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if q.qsize() > 0:
            answer.append(-q.get())
        else:
            answer.append(0)
    else:
        q.put(-x)

print('\n'.join(map(str, answer)))