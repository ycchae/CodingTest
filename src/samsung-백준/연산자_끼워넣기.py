from itertools import permutations

def calc(expr):
    while len(expr) > 1:
        op = expr[1]
        n1, n2 = expr[0], expr[2] 
        if op == '+': v = n1 + n2
        elif op == '-': v = n1 - n2
        elif op == '*': v = n1 * n2
        elif op == '/':
            f = False
            if n1 < 0: nn1 = -n1; f = True
            else: nn1 = n1
            if n2 < 0: nn2 = -n2; f = False
            else: nn2 = n2
            v = nn1 // nn2
            if f: v = -v
        del expr[0]
        del expr[0]
        expr[0] = v
    return expr[0]


import sys; input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

op = {0: '+', 1: '-', 2: '*', 3: '/'}
tmp = list(map(int, input().split()))
ops = []
for i, o in enumerate(tmp): ops.extend(op[i]*o)

max_val = -sys.maxsize
min_val = sys.maxsize
for o in set(permutations(ops)):
    expr = []
    for i, n in enumerate(nums):
        expr.append(n)
        if i != N-1: expr.append(o[i-1])
    val = calc(expr)
    if max_val < val: max_val = val
    if min_val > val: min_val = val

print(max_val)
print(min_val)
