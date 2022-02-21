import sys
input = sys.stdin.readline

N = int(input())
s = []
w = []
for _ in range(N):
    t1, t2 = map(int, input().split())
    s.append(t1)
    w.append(t2)

answer = 0
def dfs(cur):
    global answer
    if cur == N:
        cnt = 0
        for d in s:
            if d <= 0: cnt += 1
        answer = max(answer, cnt)
        return

    if s[cur] <= 0:
        dfs(cur+1)
        return

    for i in range(N):
        f = False
        if i != cur and s[i] > 0:
            f = True
            s[cur] -= w[i]
            s[i] -= w[cur]
            dfs(cur+1)
            s[cur] += w[i]
            s[i] += w[cur]
    if not f:
        dfs(cur+1)


dfs(0)
print(answer)