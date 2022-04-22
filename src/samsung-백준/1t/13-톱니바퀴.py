import sys; sys.stdin = open('../d.txt', 'r')

from collections import deque
wheel = []
for _ in range(4):
    wheel.append(deque(list(input())))
K = int(input())

def rotate(s: deque, r):
    # 시계 방향
    if r == 1: s.appendleft(s.pop())
    # 반시계 방향
    elif r == 0: s.append(s.popleft())

for _ in range(K):
    n, r = map(int, input().split())
    n -= 1
    if r == -1: r = 0

    stat = []
    for i in range(3): stat.append(wheel[i][2] != wheel[i+1][6])
    rotate(wheel[n], r); nr = (r + 1) % 2
    for i in range(n, 3):
        if stat[i]: rotate(wheel[i+1], nr); nr = (nr + 1) % 2
        else: break

    nr = (r + 1) % 2
    for i in range(n-1, -1, -1):
        if stat[i]: rotate(wheel[i], nr); nr = (nr + 1) % 2
        else: break

answer = 0
for i in range(4): answer += int(wheel[i][0]) * 2**i

print(answer)