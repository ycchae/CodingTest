import sys;
sys.stdin = open('d.txt', 'r')

from collections import defaultdict
N = int(input())
spec = defaultdict(dict)

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if i == j: continue
        spec[i][j] = v

minval = 1e9

nteam = N//2
teamW = set(range(N))
teamA = [0]

def dfs(cur, depth):
    global minval

    if depth == nteam:
        ta, tb = 0, 0
        teamB = list(teamW - set(teamA))
        for i in range(nteam):
            a1 = teamA[i]
            b1 = teamB[i]
            for j in range(i+1, nteam):
                a2 = teamA[j]
                b2 = teamB[j]
                ta += spec[a1][a2] + spec[a2][a1]
                tb += spec[b1][b2] + spec[b2][b1]

        ans = abs(ta-tb)
        if ans < minval: minval = ans
        return

    for i in range(cur+1, N):
        teamA.append(i)
        dfs(i, depth+1)
        teamA.pop()

dfs(0, 1)
print(minval)

#
#
# def combinations(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)
#
# from collections import defaultdict
# N = int(input())
# spec = defaultdict(dict)
#
# for i in range(N):
#     for j, v in enumerate(map(int, input().split())):
#         if i == j: continue
#         spec[i][j] = v
#
# minval = 1e9
#
# for comb in combinations(range(N), N//2):
#     team1, team2 = 0, 0
#     t2 = list(set(range(N)) - set(comb))
#     for i in range(N//2):
#         a1 = comb[i]
#         a2 = t2[i]
#         for j in range(i+1, N//2):
#             b1 = comb[j]
#             b2 = t2[j]
#             team1 += spec[a1][b1] + spec[b1][a1]
#             team2 += spec[a2][b2] + spec[b2][a2]
#
#     v = abs(team1 - team2)
#     if minval > v: minval = v
#
# print(minval)
