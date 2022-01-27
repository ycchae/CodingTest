import sys
input = sys.stdin.readline

N = int(input())
hights = list(map(int, input().split()))

answer = []
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > hights[i]:
            answer.append(stack[-1][0])
            break
        stack.pop()
        
    if not stack:
        answer.append(0)
    
    stack.append((i+1, hights[i]))
        
print(' '.join(map(str, answer)))
