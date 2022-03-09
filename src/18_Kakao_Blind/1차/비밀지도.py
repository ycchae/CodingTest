def solution(n, arr1, arr2):
    answer = []
    board = [arr1[i] | arr2[i] for i in range(n)]
    for r in board: answer.append(bin(r)[2:].zfill(n).replace("1","#").replace("0"," "))
    return answer

# print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

# 옛날 코드
# def solution(n, arr1, arr2):
#     answer = []
#     map = []
#     for i in range(n):
#         map.append(arr1[i] | arr2[i])
    
#     for i in range(n):
#         str = ""
#         for j in range(n):
#             if map[i] & 1 == 1:
#                 str = "#"+str
#             else:
#                 str = " "+str
#             map[i] = map[i] >> 1
#         answer.append(str)
        
#     print(answer)
#     return answer