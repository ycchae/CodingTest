def solution(N):
    if (N**0.5).is_integer():
        return 1
    for i in range(1, int(N**0.5) + 1):
        if ((N - i**2) **0.5).is_integer():
            return 2
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N - i**2)**0.5) + 1):
            if ((N - i**2 - j**2)**0.5).is_integer():
                return 3
    return 4

N = int(input())
print(solution(N))