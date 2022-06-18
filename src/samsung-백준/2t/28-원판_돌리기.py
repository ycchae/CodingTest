import sys; sys.stdin = open('d.txt', 'r')

def solution():
    N,M,T = map(int, input().split())
    circle = []
    for i in range(N):
        circle.append(list(map(int, input().split())))
            
    def move(c :list, d: int, k :int):
        if k > M//2:
            d = (d + 1) % 2
            k = M - k
        if d == 0:
            for _ in range(k):
                t = c.pop()
                c.insert(0, t)
        else:
            for _ in range(k):
                t = c.pop(0)
                c.append(t)
            
    
    dirs = [(1,0),(-1,0),(0,-1),(0,1)]
    for _ in range(T):
        x, d, k = map(int, input().split())
        for i in range(N):
            if (i + 1) % x == 0:
                move(circle[i], d, k)
        
        updated = False
        s, cnt = 0, 0
        for i in range(N):
            for j in range(M):
                num = circle[i][j]
                if num > 0:
                    s += num
                    cnt += 1
                    
                    q = [(i,j)]
                    while q:
                        r, c = q.pop()
                        for d in dirs:
                            nr = r + d[0]
                            nc = (c + d[1]) % M
                            if nr < 0 or nr >= N: continue
                            if circle[nr][nc] == num:
                                if not updated: updated = True
                                circle[nr][nc] = 0
                                q.append((nr,nc))
        
        if cnt == 0: return 0
        if updated: continue
        avg = s / cnt
        for i in range(N):
            for j in range(M):
                num = circle[i][j]
                if num > 0:
                    if num < avg:
                        circle[i][j] += 1
                    elif num > avg:
                        circle[i][j] -= 1
    
    answer = 0
    for i in range(N):
        answer += sum(circle[i])
    return answer

answers = [30,22,22,0,26]
for a in answers:
    answer = solution()
    print(answer, end=' ')
    print(answer == a)
