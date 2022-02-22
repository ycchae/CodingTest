import sys
input = sys.stdin.readline
import math

TC = int(input())
for _ in range(TC):
    N, M = map(int, input().split())
    print(int(math.factorial(M) / (math.factorial(M-N) * math.factorial(N))))