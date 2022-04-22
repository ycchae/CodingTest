import sys; sys.stdin = open('../d.txt', 'r')

from collections import deque

N,M,T = map(int, input().split())

nums = [[]]
for i in range(N):
    nums.append(deque(list(map(int, input().split()))))

def rotate(i, d, k):
    if d == 0:
        for _ in range(k):
            n = nums[i].pop()
            nums[i].appendleft(n)
    else:
        for _ in range(k):
            n = nums[i].popleft()
            nums[i].append(n)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
reverse = [1,0]
for _ in range(T):
    x, d, k = map(int, input().split())

    cand_update = set()
    for i in range(x, N+1, x):
        if k > M // 2:
            k = M - k
            d = reverse[d]
        rotate(i, d, k)

    visited = [[False] * M for _ in range(N + 1)]
    updated = False
    ss = 0
    cnt = 0
    for i in range(1, N + 1):
        for j in range(M):
            same = nums[i][j]
            if same == 0: continue
            ss += same
            cnt += 1

            if visited[i][j]: continue
            adj2 = False
            dq = deque([(i,j)])

            while dq:
                r, c = dq.popleft()
                for d in dirs:
                    nr = r + d[0]
                    nc = (c + d[1]) % M
                    if nr <= 0 or nc < 0 or nr > N or nc >= M: continue
                    if nums[nr][nc] != same: continue
                    if visited[nr][nc]: continue
                    visited[nr][nc] = True

                    nums[nr][nc] = 0
                    dq.append((nr,nc))

                    if not adj2: adj2 = True

            if adj2:
                nums[i][j] = 0
                if not updated: updated = True

    if cnt == 0: print(0); exit(0)
    if updated: continue

    avg = ss / cnt
    for i in range(1, N+1):
        for j in range(M):
            if nums[i][j] > 0:
                if nums[i][j] > avg:
                    nums[i][j] -= 1
                elif nums[i][j] < avg:
                    nums[i][j] += 1


answer = 0
for n in nums:
    answer += sum(n)
print(answer)


