from collections import defaultdict

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for s, e in path:
        graph[s].append(e)
        graph[e].append(s)
    
    parent = defaultdict(int)
    child = defaultdict(int)
    for o in order: parent[o[1]] = o[0]
    if 0 in parent.keys(): return False

    stack = [0]
    while stack:
        cur = stack.pop()
        if cur in parent.keys() and not visited[parent[cur]]:
            child[parent[cur]] = cur
            continue

        visited[cur] = True
        for next in graph[cur]:
            if not visited[next]: stack.append(next)

        if cur in child.keys():
            stack.append(child[cur])

    if False in visited:
        return False
    return True

print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))

# print(solution(9,[[0,1],[0,3],[0,7],[6,1],[3,8],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))
# print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[6,4],[4,3]]))
# print(solution(9,[[0,1],[0,3],[0,7],[8,1],[1,2],[4,7],[7,5],[4,6]], [[2,3],[8,7]]))
# print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,2],[2,6],[4,1],[6,7]]))

# from collections import defaultdict
# def dfs(node, roots, graph, tree):
#     tree[node] = roots
#     for v in graph[node]:
#         if tree[v] == 0:
#             dfs(v, roots+[node], graph, tree)

# def find(roots, x):
#     if roots[x] != x: roots[x] = find(roots, roots[x])
#     return roots[x]
# def union(roots, a,b):
#     a, b = find(roots, a), find(roots, b)
#     if a!= b: roots[b] = a

# def solution(n, path, order):
#     answer = True
#     graph = defaultdict(list)
#     for p in path:
#         s, e = p
#         graph[s].append(e); graph[e].append(s)
#     tree = [0] * n
#     dfs(0, [], graph, tree)

#     # Cyclic 찾으면 됨
#     # tmp = set()
#     # ograph = defaultdict(set)
#     # for o in order:
#     #     s,e = o
#     #     if len(tree[s]) >= len(tree[e]):
#     #         if e in tree[s]: return False
#     #         ograph[e].update(tree[s])
#     #         ograph[e].add(s)
#     #         tmp.update(ograph[e])
#     #         # warn.append(e)
#     # print(ograph)
#     # roots = [i for i in range(n)]
#     # for i in ograph:
#     #     for j in ograph[i]:
#     #         union(roots, i,j)
#     # print(set([find(roots, i) for i in range(n)]))
#     # if len(set([find(roots, i) for i in range(n)])) == n-len(tmp): return False

#     # for w in warn:
#     #     for t in ograph[w]:
#     #         if w in ograph[t]:
#     #             return False

#     return answer