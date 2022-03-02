N = int(input())
s = input()
answer = 1
first = s[0]
for i in range(0, N-1):
    if s[i] != s[i+1] and s[i] == first: answer +=1
print(answer)