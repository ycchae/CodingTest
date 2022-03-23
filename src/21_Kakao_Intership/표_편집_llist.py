def move(cur, acc, llist):
    if acc > 0:
        for _ in range(acc): cur = llist[cur][1]
    else:
        for _ in range(abs(acc)): cur = llist[cur][0]
    return cur
    
def solution(n, k, cmd):
    llist = {i: [i - 1, i + 1] for i in range(n)} # n=8 0~7까지
    state = ["O" for _ in range(n)]
    stack = []

    cur = k
    acc = 0
    for c in cmd:
        if c[0] == 'D': acc += int(c[2:])
        elif c[0] == 'U': acc -= int(c[2:])
        elif c[0] == 'C':
            cur = move(cur, acc, llist); acc = 0
            prev, next = llist[cur]
            stack.append((prev, next, cur))
            state[cur] = 'X'
            
            if next == n: cur = llist[cur][0]
            else: cur = llist[cur][1]
            
            if prev == -1: llist[next][0] = prev
            elif next == n: llist[prev][1] = next
            else: llist[prev][1] = next; llist[next][0] = prev
        elif c[0] == 'Z':
            cur = move(cur, acc, llist); acc = 0
            prev, next, p = stack.pop()
            state[p] = "O"

            if prev == -1: llist[next][0] = p
            elif next == n: llist[prev][1] = p
            else: llist[prev][1] = p; llist[next][0] = p

    return "".join(state)

# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))