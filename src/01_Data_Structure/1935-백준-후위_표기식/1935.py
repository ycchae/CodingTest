import sys
input = sys.stdin.readline

N = int(input())
EXPR = input().strip()
nums = [int(input()) for _ in range(N)]

exp = []
for s in EXPR:
    if s.isalpha():
        exp.append(nums[ord(s)-ord('A')])
    else:
        b = exp.pop()
        a = exp.pop()
        res = eval(f'{a}{s}{b}')
        exp.append(res)

print(f'{exp[0]:.2f}')