import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num_name = {}
names = []
for i in range(n):
    name = input().strip()
    num_name[name] = str(i+1)
    names.append(name)

answer = []
for _ in range(m):
    q = input().strip()
    if q[0].isalpha():
        answer.append(num_name[q])
    else:
        answer.append(names[int(q)-1])

print('\n'.join(answer))