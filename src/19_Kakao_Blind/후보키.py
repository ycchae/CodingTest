from itertools import combinations
def solution(relation):
    answer = 0
    lrow = len(relation)
    lcol = len(relation[0])
    cols = [[] for _ in range(lcol)]
    for j in range(lcol):
        for i in range(lrow):
            cols[j].append(str(relation[i][j]))
    
    candidates = list(range(lcol))
    foreign = [[] for _ in range(lcol+1)]
    for n in range(1, lcol+1):
        for comb in combinations(candidates, n):
            fkey = set(comb)

            p = False
            for k in range(n):
                if any(f.issubset(fkey) for f in foreign[k]): p = True
            if p: continue
                
            new_col = ["" for _ in range(lrow)]
            for i in range(lrow):
                for c in fkey:
                    new_col[i] += cols[c][i]
                        
            if len(set(new_col)) == lrow: foreign[n].append(fkey); answer += 1

    return answer

print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))
# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))