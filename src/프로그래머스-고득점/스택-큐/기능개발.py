def solution(progresses, speeds):
    answer = []
    import math
    l = len(progresses)
    days = list(map(lambda x: math.ceil((100 - progresses[x]) / speeds[x]), range(l)))
    front = 0
    for idx in range(l):
        if days[idx] > days[front]:
            answer.append(idx - front)
            front = idx
    answer.append(l - front)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# 다른 사람 풀이
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]