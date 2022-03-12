import heapq
def solution(food_times, k):
    answer = -1
    lf = len(food_times)
    heap = []
    for i, f in enumerate(food_times): heapq.heappush(heap, (f, i+1))
    ate = 0

    while heap:
        t = (heap[0][0] - ate) * lf
        if k >= t:
            k -= t
            ate, _ = heapq.heappop(heap)
            lf -= 1
        else:
            heap.sort(key=lambda x: x[1])
            answer = heap[k%lf][1]
            break

    return answer
                

print(solution([3, 1, 2], 5))