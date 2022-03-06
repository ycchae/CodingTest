def solution(n, lost, reserve):
    nlost = set(lost) - set(reserve)
    nreserve = set(reserve) - set(lost)
    answer = n - len(nlost)

    for l in nlost:
        if l - 1 in nreserve:
            nreserve.remove(l-1)
            answer += 1
        elif l + 1 in nreserve:
            nreserve.remove(l+1)
            answer += 1
    return answer

print(solution(5,[2,4],[1,3,5]))
print(solution(5,[2,4],[3]))
print(solution(3,[3],[1]))

print(solution(5,[1,2,3,4,5],[1,3,5]))
