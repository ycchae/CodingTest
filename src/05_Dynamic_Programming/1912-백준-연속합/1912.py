N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1, N): dp.append(max(dp[i-1] + arr[i], arr[i]))
print(max(dp))