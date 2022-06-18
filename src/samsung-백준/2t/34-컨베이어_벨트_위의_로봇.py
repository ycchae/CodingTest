import sys; sys.stdin = open('d.txt', 'r')

N, K = map(int, input().split())
broken = 0
MAX_N = 2*N

belt = list(map(int, input().split()))
op = 0
dp = N-1

robots = []
located = [0]*MAX_N

def rotate():
    global robots
    belt.insert(0, belt.pop())
    
    nrobots = []
    for i in range(len(robots)):
        rpos = robots[i]
        located[rpos] -= 1
        nrpos = (rpos + 1) % (MAX_N)
        if nrpos != dp:
            nrobots.append(nrpos)
            located[nrpos] += 1
    robots = nrobots

def move():
    global broken, robots
    if not robots: return
    nrobots = []
    for i in range(len(robots)):
        rpos = robots[i]
        located[rpos] -= 1
        nrpos = (rpos + 1) % (MAX_N)
        if not located[nrpos] and belt[nrpos] > 0:
            belt[nrpos] -= 1
            if belt[nrpos] == 0: broken += 1

            if nrpos != dp:
                nrobots.append(nrpos)
                located[nrpos] += 1
        else:
            nrobots.append(rpos)
            located[rpos] += 1
    robots = nrobots

answer = 0
while True:
    answer += 1
    rotate()
    move()
    if belt[op] > 0:
        located[op] += 1
        robots.append(op)
        belt[op] -= 1
        if belt[op] <= 0: broken += 1

    if broken >= K: break

print(answer)