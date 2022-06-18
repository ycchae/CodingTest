import sys; sys.stdin = open('d.txt' ,'r')

N, M, H = map(int, input().split())

ladder = [[0]*N for _ in range(H)]
nline = [0]*(N-1)
for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    ladder[a][b] = 1
    nline[b] += 1

def check():
    for j in range(N):
        cur = j
        for i in range(H):
            if ladder[i][cur]:
                cur += 1
            elif cur-1 >= 0 and ladder[i][cur-1]:
                cur -= 1
        if cur != j:
            return False
    return True

quit = False
def dfs(depth, r,c):
    global quit
    if quit: return
    if depth == n:
        quit = check()
        return
    
    odd = 0
    for nl in nline:
        if nl % 2 == 1: odd += 1
    if odd > n - depth: return
    
    for i in range(r, H):
        if i == r: k = c
        else: k = 0
        for j in range(k, N-1):
            # 왼쪽에 사다리 없고, 오른쪽에 사다리 없고, 검사하는곳 사다리 없고
            if (j - 1 >= 0 and ladder[i][j - 1]) \
                or ladder[i][j + 1] or ladder[i][j]: continue
            ladder[i][j] = 1
            nline[j] += 1
            dfs(depth+1, i,j+2)
            ladder[i][j] = 0
            nline[j] -= 1

for n in range(4):
    dfs(0, 0,0)
    if quit: answer = n; break
if not quit:
    answer = -1
print(answer)