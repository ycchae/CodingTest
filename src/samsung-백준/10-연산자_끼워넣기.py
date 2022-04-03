import sys; sys.stdin = open('d.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
add, minus, product, divide = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(num, idx, add, minus, product, divide):
    global max_val, min_val
    if idx == N:
        if max_val < num: max_val = num
        if min_val > num: min_val = num
        return

    if add > 0:
        dfs(num+nums[idx], idx+1, add-1, minus, product, divide)
    if minus > 0:
        dfs(num-nums[idx], idx+1, add, minus-1, product, divide)
    if product > 0:
        dfs(num*nums[idx], idx+1, add, minus, product-1, divide)
    if divide > 0:
        dfs(int(num/nums[idx]), idx+1, add, minus, product, divide-1)

dfs(nums[0], 1, add, minus, product, divide)

print(max_val)
print(min_val)
