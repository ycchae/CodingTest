def solution(name):
    answer = 0
    min_move = len(name)-1
    while name[min_move] == 'A' and min_move > 0: min_move -= 1
    if min_move < 0: return answer

    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) +1)
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        print(c, min_move, 2*i + len(name) - next, 2*(len(name)-next) +i)
        min_move = min(min_move, 2*i + len(name) - next, 2*(len(name)-next) +i)
        
    answer += min_move

    return answer

# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("BAAA"))
# print(solution("AZAAZ"))
# print(solution("BAABAAABA"))
print(solution("ABABAAABAAAAAAABA"))