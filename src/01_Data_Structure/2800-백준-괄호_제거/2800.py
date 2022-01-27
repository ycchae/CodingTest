import sys
expr = sys.stdin.readline().strip()
answer = set()

start = []
pos = []
for i, c in enumerate(expr):
    if c == '(':
        start.append(i)
    elif c == ')':
        pos.append( (start.pop(), i) )

def remove_parentheses(comb):
    temp = list(expr)
    for c in comb:
        temp[c[0]] = ''
        temp[c[1]] = ''
    return ''.join(temp)

import itertools
for i in range(1, len(pos)+1):
    combis = itertools.combinations(pos, i)
    for comb in combis:
        answer.add(remove_parentheses(comb))

print('\n'.join(sorted(answer)))