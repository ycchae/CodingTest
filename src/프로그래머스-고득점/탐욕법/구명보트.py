def solution(people, limit):
    answer = 0
    lp = len(people)
    speople = sorted(people, reverse=True)
    cnt = 0
    for i in range(lp):
        if cnt >= lp: break
        if limit - speople[i] >= 40:
            if speople[i] + speople[-1] <= limit:
                cnt += 1
                del speople[-1]
        answer += 1
        cnt += 1
    return answer


print(solution([70, 50, 80, 50],100))
print(solution([70, 50, 80],100))