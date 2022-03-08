from itertools import permutations
def solution(expression):
    answer = 0
    expressions = []
    ops = {}
    tmp = ''
    for e in expression:
        if e == '-' or e == '+' or e == '*':
            expressions.append(int(tmp)); tmp = ''
            expressions.append(e)
            
            if not ops.get(e): ops[e] = 0
            ops[e] += 1

        else: tmp += e
    expressions.append(int(tmp))

    for per in permutations(ops.keys()):
        op = 0
        cnt = 0
        exps = expressions[:]
        while len(exps) > 1:
            idx = exps.index(per[op])
            
            val = -1
            if per[op] == '*':
                val = exps[idx-1] * exps[idx+1]  
            elif per[op] == '+':
                val = exps[idx-1] + exps[idx+1]
            elif per[op] == '-':
                val = exps[idx-1] - exps[idx+1]

            for _ in range(3):
                del exps[idx-1]
            exps.insert(idx-1, val)

            cnt += 1
            if ops[per[op]] == cnt:
                cnt = 0
                op += 1

        answer = max(answer, abs(exps[0]))
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))