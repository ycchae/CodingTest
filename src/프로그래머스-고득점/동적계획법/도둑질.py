def solution(money):
    dp = [0] * len(money)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
    max1 = max(dp)
    
    dp = [0] * len(money)
    dp[0] = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], money[i] + dp[i-2])
    max2 = max(dp)

    if max1 > max2: return max1
    else: return max2


print(solution([1, 2, 3, 1]))