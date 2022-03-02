import sys
input = sys.stdin.readline

N, M = map(int, input().split())

grades = []
scores = []
for _ in range(N):
    g, s = input().split()
    grades.append(g)
    scores.append(int(s))

import bisect
answer = []
for _ in range(M):
    test = int(input())
    i = bisect.bisect_left(scores, test)
    
    answer.append(grades[i])

print('\n'.join(answer))