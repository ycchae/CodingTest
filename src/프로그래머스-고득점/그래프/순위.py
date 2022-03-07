def solution(n, results):
    answer = 0
    wins = [set() for _ in range(n)]
    loses = [set() for _ in range(n)]
    for result in results:
        win, lose = map(lambda x: x-1, result)
        wins[win].add(lose)
        loses[lose].add(win)

    for i in range(n):
        for win in wins[i]:
            loses[win].update(loses[i])
        for lose in loses[i]:
            wins[lose].update(wins[i])
    
    for i in range(n):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))