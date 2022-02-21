N, k = int(input()), int(input())

start, end = 1, k

answer = 0
while start <= end:
    mid = (start + end) // 2

    num = 0
    for i in range(1, N+1):
        num += min(mid//i, N)

    if k > num:
        start = mid +1
    else:
        answer = mid
        end = mid -1
print(answer)