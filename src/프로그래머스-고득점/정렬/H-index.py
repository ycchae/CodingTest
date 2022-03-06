def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)

print(solution([3, 0, 6, 1, 5]))
print(solution([6,6,6,6,6,6,7,5]))