import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

answer = 0
while start <= end:
    mid = (start + end) // 2

    get = sum([t-mid if mid < t else 0 for t in trees])
    if get >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)