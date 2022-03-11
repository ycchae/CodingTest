from functools import reduce
import sys; input=sys.stdin.readline
import math

N = int(input())
stu = list(map(int, input().split()))
B, C = map(int, input().split())

stu = map(lambda x: 0 if x-B <= 0 else x-B, stu)
answer = reduce(lambda acc, cur: acc + math.ceil(cur / C), stu, N)
print(answer)