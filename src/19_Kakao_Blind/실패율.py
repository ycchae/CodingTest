import heapq
def solution(N, stages):
    answer = []
    heap = []
    stages.sort()
    luser = len(stages)
    i = 0
    for s in range(1,N+1):

        while i < luser and stages[i] < s: i += 1
        not_arrived = i
        arrived = luser - not_arrived

        while i < luser and stages[i] == s: i += 1
        not_cleared = i - not_arrived

        if arrived: failure = not_cleared / arrived
        else: failure = 0
        
        heapq.heappush(heap, (-failure, s))
        
    for e in list(heapq.nsmallest(N, heap)): answer.append(e[1])
    return answer

# print(solution(5, [2,1,1,2]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))