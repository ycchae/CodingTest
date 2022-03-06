def solution(routes):
    answer = 0
    lr = len(routes)
    routes.sort(key=lambda x: x[1])
    cnt = 0
    i = 0
    while i < lr:
        if cnt == lr:
            break
        cam = routes[i][1]
        for j in range(i+1, lr):
            if routes[j][0] > cam: break
            cnt += 1
            i = j
        cnt += 1
        answer += 1
        i += 1
    return answer

# print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
# print(solution([[-18,-17],[-20,-19],[-20,-15], [-14,-5], [-16,-13], [-5,-3]]))
# print(solution([[-20,-5],[-20,-19],[-17,-14],[-16,-3]]))
# print(solution([[-20,-15],[-19,-12],[-14,-5],[-18,-13],[-7,-6],[-5,-3]]))
print(solution([[-20,-19],[-17,-14],[-20,-5],[-16,-3],[-4,0]]))