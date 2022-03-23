import bisect
def moving(sdeleted, mm, cur, n):
    origin = cur
    if mm < 0:
        while mm < 0:
            to = cur + mm
            num_false = cur - to - (bisect.bisect_right(sdeleted,cur) - bisect.bisect_right(sdeleted,to))
            mm += num_false
            cur = to
        
    elif mm > 0:
        while mm > 0:
            to = cur + mm
            num_false = to - cur - (bisect.bisect_left(sdeleted,to) - bisect.bisect_left(sdeleted,cur))
            mm -= num_false
            cur = to
        if cur >= n: return origin
    return cur

def solution(n, k, cmds):
    cur = k
    move = 0
    is_deleted = [False] * n
    deleted = []
    sdeleted = []

    for cmd in cmds:
        c = cmd.split(' ')
        
        # print(c)
        if c[0] == 'D':
            move += int(c[1])
        if c[0] == 'U':
            move -= int(c[1])
        if c[0] == 'C':
            cur = moving(sdeleted, move, cur, n)
            move = 0
            d = cur
            
            nc = moving(sdeleted, 1, cur, n)
            if nc == cur: nc = moving(sdeleted, -1, cur, n)
            cur = nc
            
            is_deleted[d] = True
            deleted.append(d)
            sdeleted.insert(bisect.bisect_left(sdeleted, d), d)
            
        if c[0] == 'Z':
            cur = moving(sdeleted, move, cur, n)
            move = 0
            
            p = deleted.pop()
            is_deleted[p] = False
            del sdeleted[bisect.bisect_left(sdeleted, p)]

    return ''.join(['X' if d else 'O' for d in is_deleted])

# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
