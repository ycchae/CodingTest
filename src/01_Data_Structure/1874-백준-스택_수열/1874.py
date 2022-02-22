import sys
input = sys.stdin.readline

N = int(input())
arr = [ int(input()) for _ in range(N) ]

stack = []
stack_max = 0

answer = []
cur = 0
for i in range(N):
    n = i + 1
    if n <= arr[cur]:
        stack.append(n)
        stack_max = n
        answer.append('+')

    while cur < N and len(stack) > 0 and stack[-1] == arr[cur]:
        stack.pop()
        cur += 1
        answer.append('-')
    
    if cur < N and arr[cur] < stack_max:
        print("NO")
        exit(0)

print('\n'.join(answer))