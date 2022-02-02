import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

start, end = 0, max(budgets)
while start <= end:
    mid = (start + end) // 2

    money = sum([ b if b < mid else mid for b in budgets ])
    if money <= total_budget:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
