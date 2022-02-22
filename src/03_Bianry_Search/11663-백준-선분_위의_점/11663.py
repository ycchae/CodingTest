import sys
input = sys.stdin.readline
N,M = map(int, input().split())
dots = sorted(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]

from bisect import bisect_left, bisect_right
for line in lines: print(bisect_right(dots, line[1]) - bisect_left(dots, line[0]))