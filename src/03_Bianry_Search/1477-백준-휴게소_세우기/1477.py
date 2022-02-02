import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(L)
arr.sort()

start, end = 1, L-1

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > mid:
            count += (arr[i] - arr[i-1] -1) // mid
    if count > M:
        start = mid + 1
    else:
        answer = mid
        end = mid -1

print(answer)