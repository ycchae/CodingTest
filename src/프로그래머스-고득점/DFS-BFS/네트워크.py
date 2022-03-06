def find(root, x):
    if root[x] != x: root[x] = find(root, root[x])
    return root[x]

def solution(n, computers):
    answer = n
    root = [i for i in range(n)]
    for i in range(n):
        j = i+1
        for val in computers[i][i+1:]:
            if val == 1:
                sroot = find(root, i)
                eroot = find(root, j)
                if sroot != eroot:
                    root[sroot] = eroot
                    answer -= 1
            j += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))