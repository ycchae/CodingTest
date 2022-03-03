def solution(priorities, location):
    answer = 0
    remains = list(map(lambda x: priorities.count(x), range(0, 10)))
    from collections import deque
    q = deque( zip(priorities, range(len(priorities))) )
    while q:
        priority, num = q.popleft()
        if sum(remains[priority+1:]) > 0: q.append((priority, num))
        else:
            if num == location: return answer + 1
            answer += 1
            remains[priority] -= 1
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))