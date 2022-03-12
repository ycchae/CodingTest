import sys; input = sys.stdin.readline

N = int(input())
time = [0]*(N+1)
price = [0]*(N+1)
for i in range(N):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if i + time[i] <= N: dp[i] = max(price[i] + dp[i + time[i]], dp[i+1])
    else: dp[i] = dp[i+1]

print(dp[0])