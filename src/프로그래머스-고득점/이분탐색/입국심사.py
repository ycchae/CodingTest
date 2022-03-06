def solution(n, times):    
    start, end = min(times), n*max(times)
    answer = end

    while start <= end:
        mid = (start + end) // 2
        people = sum(mid // i for i in times)
        if people < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = min(answer, mid)
    return answer

print(solution(6,[7,10]))