import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations

answer = 0
for i in range(1, N+1):
    for comb in combinations(arr, i):
        if sum(comb) == S:
            answer += 1

print(answer)
