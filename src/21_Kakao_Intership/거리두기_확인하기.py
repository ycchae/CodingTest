from collections import deque, defaultdict

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def guriguri(people, partitions):
    dq = deque()
    lpeople = list(people.keys())
    for r,c in lpeople:
        visited = defaultdict(bool)
        dq.append((r,c,0))
        visited[(r,c)] = True
        while dq:
            r,c,depth = dq.popleft()
            if depth >= 2: continue
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr < 0 or nc < 0 or nr >=5 or nc >= 5: continue
                if partitions[(nr,nc)]: continue
                if visited[(nr,nc)]: continue
                if people[(nr,nc)]: return 0
                visited[(nr,nc)] = True
                dq.append((nr, nc, depth+1))
    return 1

def solution(places):
    answer = []
    r = 0
    for room in places:
        print('r', r)
        r += 1
        people = defaultdict(bool)
        partitions = defaultdict(bool)
        for r, row in enumerate(room):
            for c, col in enumerate(row):
                if col == 'P': people[(r,c)] = True
                elif col == 'X': partitions[(r,c)] = True
        answer.append(guriguri(people,partitions))
    return answer