import sys
import heapq

def get_stat(trstat, idx):
    return (trstat >> idx) & 1
def toggle_stat(trstat, idx):
    return trstat ^ (1 << idx)
    
INF = sys.maxsize
def solution(n, start, end, roads, traps):
    answer = 0
    trap_idx = {value:i for i,value in enumerate(traps)}
    
    edges = [[] for _ in range(n+1)]
    for u,v,d in roads:
        edges[u].append((v, d, 0))
        edges[v].append((u, d, 1))
    
    trstat = 0b0
    dists = [[INF]*(2**len(traps)) for _ in range(n+1)]
    dists[start][trstat] = 0
    
    hq = [(0, start, trstat)]
    while hq:
        cdist, u, trstat = heapq.heappop(hq)
        
        if u == end: answer = cdist; break
        if dists[u][trstat] < cdist: continue
        for v, ndist, rev in edges[u]:
            tdist = cdist + ndist
            ntrstat = trstat
            # u is trap
            if u in trap_idx:
                ustat = get_stat(trstat, trap_idx[u])
                # v is trap
                if v in trap_idx:
                    vstat = get_stat(trstat, trap_idx[v])
                    reverse = vstat ^ ustat
                    
                    ntrstat = toggle_stat(trstat, trap_idx[v])
                # v is not trap
                else:
                    reverse = ustat
            # u is not trap
            else:
                # v is trap
                if v in trap_idx:
                    reverse = get_stat(trstat, trap_idx[v])
                    
                    ntrstat = toggle_stat(trstat, trap_idx[v])
                # v is not trap
                else:
                    reverse = 0
            
            if reverse == rev:
                if dists[v][ntrstat] > tdist:
                    dists[v][ntrstat] = tdist
                    heapq.heappush(hq, (tdist, v, ntrstat))
    # print(dists)
    return answer

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(3, 1, 3, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], ))