def solution(brown, yellow):
    answer = []
    total = brown + yellow
    divisors = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisors.append(i)
        
    j = 0
    while j <= len(divisors)//2:
        col = divisors[len(divisors)-j-1]+2
        row = divisors[j]+2
        if col * row == total:
            answer = [col, row]
            break
        j += 1
        
    return answer
    
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))