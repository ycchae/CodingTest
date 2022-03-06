def find(root, x):
    if x != root[x]: root[x] = find(root, root[x])
    return root[x]

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    root = [i for i in range(n)]
    cnt = 0
    for info in costs:
        if cnt == n-1: break
        start, end, cost = info
        sroot = find(root, start)
        eroot = find(root, end)
        if sroot != eroot:
            root[sroot] = eroot
            answer += cost
            cnt += 1
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[2,3,8]]))
print(solution(4,[[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))