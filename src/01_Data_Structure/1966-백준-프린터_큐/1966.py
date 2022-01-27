import sys
input = sys.stdin.readline

import queue

TC = int(input())


for _ in range(TC):
    n, target = map(int, input().split())
    priorities = list(map(int, input().split()))
    order = reversed(sorted(priorities))
    answered = False

    q = queue.Queue()
    
    for i in range(n):
        q.put((priorities[i], i))

    count = 1
    for o in order:

        while True:
            elem = q.get()
            if o == elem[0]:
                if elem[1] == target:
                    answered = True
                    print(count)
                break
            q.put(elem)

        if answered:
            break
        count += 1
    