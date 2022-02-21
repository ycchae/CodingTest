import sys
input = sys.stdin.readline

import bisect

N = int(input())
target = sorted((map(int, input().split())))
_ = input()
cards = map(int, input().split())

answer = []
for c in cards:
    idx = bisect.bisect_left(target, c)
    if idx >= N or target[idx] != c:
        answer.append(0)
    elif target[idx] == c:
        answer.append(1)

print(' '.join(map(str, answer)))