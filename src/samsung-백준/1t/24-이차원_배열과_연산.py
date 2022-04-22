import sys; sys.stdin = open('../d.txt', 'r')

from collections import defaultdict

r,c,k = map(int, input().split())
r -= 1; c -= 1

R, C = 3, 3
A = defaultdict(lambda: defaultdict(int))
for i in range(3):
    for j, v in enumerate(list(map(int, input().split()))):
        A[i][j] = v

def rop():
    global C
    tmpC = C

    for i in range(R):
        count = defaultdict(int)
        for j in range(tmpC):
            if A[i][j] != 0:
                count[A[i][j]] += 1

        nums = list(count.keys())
        nums.sort(key = lambda x: (count[x], x))

        nC = len(nums) * 2
        nn = 0
        A[i] = defaultdict(int)
        for j in range(0, nC, 2):
            n = nums[nn]
            A[i][j] = n
            A[i][j+1] = count[n]
            nn += 1

        if C < nC: C = nC

def cop():
    global R

    tmpR = R
    for j in range(C):
        count = defaultdict(int)
        for i in range(tmpR):
            if A[i][j] != 0:
                count[A[i][j]] += 1

        nums = list(count.keys())
        nums.sort(key = lambda x: (count[x], x))

        nR = len(nums) * 2
        nn = 0

        for i in range(0, nR, 2):
            n = nums[nn]
            A[i][j] = n
            A[i+1][j] = count[n]
            nn += 1
        for i in range(nR, R):
            A[i][j] = 0

        if R < nR: R = nR

t = 0
while not (r < R and c < C and A[r][c] == k):
    if R >= C:
        rop()
    else:
        cop()
    t += 1
    if t == 101: t = -1; break

print(t)