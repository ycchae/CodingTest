def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            small = heapq.heappop(scoville)
            second_small = heapq.heappop(scoville)
        except:
            return -1
        new_s = small + second_small*2
        heapq.heappush(scoville, new_s)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))