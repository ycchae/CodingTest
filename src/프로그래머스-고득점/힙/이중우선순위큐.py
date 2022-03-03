from heapq import heappop, heappush

def update(heap, visited):
    while heap and visited[heap[0][1]] == False:
        heappop(heap)

def solution(operations):
    answer = []

    visited = [False] * len(operations)
    maxheap = []
    minheap = []

    for i, operation in enumerate(operations):
        op, num = operation.split()
        num = int(num)

        if op == "I":
            heappush(maxheap, (-num, i))
            heappush(minheap, (num, i))
            visited[i] = True
        elif op == "D":
            if num == 1:
                update(maxheap, visited)
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heappop(maxheap)
            elif num == -1:
                update(minheap, visited)
                if minheap:
                    visited[minheap[0][1]] = False
                    heappop(minheap)

    if True in visited:
        update(maxheap, visited)
        update(minheap, visited)
        answer = [-maxheap[0][0], minheap[0][0]]
    else:
        answer = [0, 0]
    return answer

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))