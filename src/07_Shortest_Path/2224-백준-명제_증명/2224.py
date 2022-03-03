import sys
input = sys.stdin.readline
N = int(input())
tot = ord('z')-ord('A')+1
graph = [[0]*tot for _ in range(tot)]
base = ord('A')
for _ in range(N):
    line = input().rstrip()
    s,e = ord(line[0])-base, ord(line[-1])-base
    graph[s][e] = 1

for k in range(tot):
    for i in range(tot):
        for j in range(tot):
            if graph[i][j] == 1 or (graph[i][k] and graph[k][j]): graph[i][j] = 1

answer = []
for s in range(tot):
    for e in range(tot):
        if graph[s][e] == 1 and s != e:
            answer.append(chr(s+base)+' => '+chr(e+base))
print(len(answer))
print('\n'.join(answer))