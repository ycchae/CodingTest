import heapq

def move(acc, left, right):
    if acc > 0:
        for _ in range(acc):
            # 오른쪽 heap에서 왼쪽 heap으로 값을 이동시킨다.
            if right: heapq.heappush(left, -heapq.heappop(right))
    else:
        for _ in range(abs(acc)):
            # 왼쪽 heap에서 오른쪽 heap으로 값을 이동시킨다.
            heapq.heappush(right, -heapq.heappop(left))
    
def solution(n, k, cmd):
    # cur: right의 맨 앞
    left, right, delete = [], [], []
    # 왼쪽은 최대값이 맨 앞에 위치하도록, 오른쪽은 최솟값이 맨 앞에 위치하도록 heap을 구성한다.
    for i in range(n): heapq.heappush(right, i)
    for i in range(k): heapq.heappush(left, -heapq.heappop(right))

    acc = 0
    for c in cmd:
        # U or D인 경우w
        sp = c.split()
        if sp[0] == 'D':
            acc += int(sp[1])
        elif sp[0] == 'U':
            acc -= int(sp[1])
        elif sp[0] == "C":
            move(acc, left, right); acc =0
            
            delete.append(heapq.heappop(right))
            if not right: heapq.heappush(right, -heapq.heappop(left))
            
        elif sp[0] == "Z":
            move(acc, left, right); acc =0
            
            repair = delete.pop()
            if repair < right[0]: heapq.heappush(left, -repair)
            else: heapq.heappush(right, repair)
            
    result = set()
    while left: result.add(-heapq.heappop(left))
    while right: result.add(heapq.heappop(right))
    answer = ["O" if i in result else "X" for i in range(n)]
    return "".join(answer)
    
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
