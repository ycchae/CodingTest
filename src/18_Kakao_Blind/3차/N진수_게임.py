def solution(n, t, m, p):
    answer = ''

    num = {i:str(i) for i in range(10)}
    num[10],num[11],num[12],num[13],num[14],num[15] = 'A','B','C','D','E','F'

    cnt = 0
    next = 0
    total = ''
    while cnt < t:
        cur = next
        s = ''
        while cur >= n:
            s = num[cur % n] + s
            cur = cur // n
        s = num[cur] + s
        total += s

        for i in range(p-1 + cnt*m, len(total), m):    
            answer += total[i]
            cnt += 1
            if cnt >= t: break
        
        next += 1
        
    return answer

print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))