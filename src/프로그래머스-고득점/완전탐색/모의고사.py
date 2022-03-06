def solution(answers):
    answer = []
    
    pt1 = [1,2,3,4,5]
    pt2 = [2,1,2,3,2,4,2,5]
    pt3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    for idx, a in enumerate(answers):
        if pt1[idx % len(pt1)] == a: score[0] += 1
        if pt2[idx % len(pt2)] == a: score[1] += 1
        if pt3[idx % len(pt3)] == a: score[2] += 1
    
    max_sc = max(score)
    for idx, s in enumerate(score):
        if s == max_sc: answer.append(idx+1)

    return sorted(answer)

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]))