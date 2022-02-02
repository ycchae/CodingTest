import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lans = []
for _ in range(N):
    lans.append(int(input()))

start, end = 1, sum(lans)

while start <= end:
    mid = (start + end) // 2

    if sum(lan // mid for lan in lans) >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)