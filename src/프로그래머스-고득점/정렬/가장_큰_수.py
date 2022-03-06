def solution(numbers):
    snums = list(map(str, numbers))
    snums.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(snums)))

print(solution([6,10,2]))
print(solution([31,30,34,5,9]))