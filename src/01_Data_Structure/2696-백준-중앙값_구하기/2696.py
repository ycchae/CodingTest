import sys
input = sys.stdin.readline

N = int(input())

answer = []
for i in range(N):
    M = int(input())    
    answer.append((M//2 +1, []))
    
    arr = []
    for _ in range(M//10 +1):
        arr.extend(list(map(int, input().split())))
    
    for j in range(M):
        if j % 2 == 0:
            middle = sorted(arr[:j+1])[(j+1)//2]
            answer[i][1].append(middle)

for i in range(N):
    num_odd = answer[i][0]
    print(num_odd)

    for j in range(num_odd//10 +1):
        if len(answer[i][1]) > j*10+10:
            print(' '.join(map(str, answer[i][1][j*10:j*10+10])))
        else:
            print(' '.join(map(str, answer[i][1][j*10:])))