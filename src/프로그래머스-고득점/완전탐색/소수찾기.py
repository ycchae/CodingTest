import math
def is_prime(x):
    if x < 2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

def solution(numbers):
    answer = 0
    from itertools import permutations
    s = set()
    for l in range(1, len(numbers)+1):
        s.update(set(map(lambda x: int(''.join(x)), permutations(numbers, l))))
    for n in s:
        if is_prime(n): answer += 1
    return answer

print(solution("17"))
print(solution("011"))

# 다른 사람 풀이
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)
