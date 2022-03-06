from re import A
from tabnanny import check


def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        all_cases = set()
        concat = int(str(N)*i)
        all_cases.add(concat)

        for j in range(0, i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all_cases.add(op1 - op2)
                    all_cases.add(op1 + op2)
                    all_cases.add(op1 * op2)
                    if op2 != 0:
                        all_cases.add(op1 // op2)
        
        if number in all_cases:
            return i
   
        dp.append(all_cases)

    return answer

print(solution(5,12))
print(solution(2,11))