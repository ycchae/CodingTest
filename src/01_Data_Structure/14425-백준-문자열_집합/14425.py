import sys
input = sys.stdin.readline

n,m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input().strip())

answer = 0
for _ in range(m):
    i = input().strip()
    if i in s:
        answer += 1

print(answer)