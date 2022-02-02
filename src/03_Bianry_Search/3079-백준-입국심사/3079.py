import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

start, end = min(arr), max(arr)*M
answer = end

while start <= end:
    mid = (start + end) // 2
    
    t = sum(mid // i for i in arr)
        
    if t < M:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer, mid)

print(answer)