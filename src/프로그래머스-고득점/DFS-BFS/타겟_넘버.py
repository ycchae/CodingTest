answer = 0
def dfs(numbers, target, depth):
    global answer
    if len(numbers) == depth:
        if sum(numbers) == target: answer += 1
        return

    numbers[depth] *= -1
    dfs(numbers, target, depth+1)
    numbers[depth] *= -1
    dfs(numbers, target, depth+1)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target,0)
    return answer

print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))

# 옛날 코드
# answer = 0
# def dfs(numbers, target, depth):
#     global answer
#     if depth == len(numbers):
#         if sum(numbers) == target:
#             answer += 1
#     else:
#         numbers[depth] *= -1
#         dfs(numbers, target, depth+1)
#         numbers[depth] *= -1
#         dfs(numbers, target, depth+1)
# def solution(numbers, target):  
#     dfs(numbers, target, 0)
#     return answer