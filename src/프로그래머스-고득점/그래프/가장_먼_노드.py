from collections import deque
def solution(n, edge):
    answer = 0
    distances = [False]*n
    distances[0] = True
    graph = [[] for _ in range(n)]

    dq = deque([])
    for e in edge:
        start, end = e[0]-1, e[1]-1
        graph[start].append(end)
        graph[end].append(start)
        if start == 0:
            dq.append((end, 1))
            distances[end] = 1
        elif end == 0:
            dq.append((start, 1))
            distances[start] = 1
    
    while dq:
        cur, cnt = dq.popleft()
        for next in graph[cur]:
            if not distances[next]:
                distances[next] = cnt+1
                dq.append((next, cnt+1))
    
    answer = distances.count(max(distances))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(4, [[1, 4], [4, 3], [1, 2]]))
print(solution(4, [[4, 3],[1,2]]))