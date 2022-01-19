instr = [int(i) for i in input().split(' ')]
N = instr[0]
K = instr[1]

answer = []

q = []
for i in range(1, N+1):
    q.append(i)

i = 0
while len(q):
    i = i + K-1
    if i >= len(q):
        i = i % len(q)
    answer.append(q.pop(i))

print(f"<{', '.join(map(str, answer))}>")