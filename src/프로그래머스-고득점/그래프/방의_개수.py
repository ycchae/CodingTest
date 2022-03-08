# https://pf333.tistory.com/86

from collections import defaultdict, deque

def solution(arrows):
    answer = 0
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

    cur = (0, 0)
    dq = deque([cur])
    for arrow in arrows:
        for _ in range(2):
            next = (cur[0] + directions[arrow][0], cur[1] + directions[arrow][1])
            dq.append(next)
            cur = next

    visited = defaultdict(int)
    visited_dir = defaultdict(int)
    cur = dq.popleft()
    visited[cur] = 1
    while dq:
        next = dq.popleft()
        if visited[next]:
            if not visited_dir[(cur,next)]: answer += 1
        else: visited[next] = 1
        visited_dir[(cur,next)] = 1
        visited_dir[(next,cur)] = 1
        cur = next

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))