import sys; sys.stdin = open('../d.txt', 'r')

from collections import deque

N, K = map(int, input().split())
broken = 0
MAX_N = 2*N

belt = deque(map(int, input().split()))
op = 0
dp = N-1

robots = deque([])
located = [False]*MAX_N

def rotate():
    belt.appendleft(belt.pop())
    for i in range(len(robots)):
        rpos = robots.popleft()
        located[rpos] = False
        nrpos = (rpos + 1) % (MAX_N)
        if nrpos != dp:
            robots.append(nrpos)
            located[nrpos] = True

def move():
    global broken
    if not robots: return
    for i in range(len(robots)):
        rpos = robots.popleft()
        located[rpos] = False
        nrpos = (rpos + 1) % (MAX_N)
        if not located[nrpos] and belt[nrpos] >= 1:
            belt[nrpos] -= 1
            if belt[nrpos] <= 0: broken += 1

            if nrpos != dp:
                robots.append(nrpos)
                located[nrpos] = True
        else:
            robots.append(rpos)
            located[rpos] = True

answer = 0
while True:
    answer += 1
    rotate()
    move()
    if belt[op] > 0:
        located[op] = True
        robots.append(op)
        belt[op] -= 1
        if belt[op] <= 0: broken += 1

    if broken >= K: break

print(answer)

