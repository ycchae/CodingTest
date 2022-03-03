import heapq
def solution(jobs):
    answer = 0
    heap = []
    jobs.sort()
    now = jobs[0][0]
    start = -1
    done = 0

    while done < len(jobs):
        for arr, time in jobs[done:]:
            if start < arr <= now:
                heapq.heappush(heap, (time, arr))
        if heap:
            cur_time, cur_arr = heapq.heappop(heap)
            start = now
            now += cur_time
            answer += (now - cur_arr)
            done += 1
        else:
            now += 1
    
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
