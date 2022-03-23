def solution(gems):
    sgems = set(gems)
    all_types = len(sgems)
    lg = len(gems)

    min_buy = lg+1
    contained = {}
    start, end = 0, 0
    
    while end < lg:
        if gems[end] not in contained:
            contained[gems[end]] = 1
        else: contained[gems[end]] += 1
        end += 1

        if len(contained) == all_types:
            while start < end:
                if contained[gems[start]] > 1:
                    contained[gems[start]] -= 1
                    start += 1
                elif min_buy > end - start:
                    min_buy = end - start
                    answer = [start+1, end]
                    break
                else: break
    return answer
                
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))


# def solution(gems):
#     sgems = set(gems)
#     all_types = len(sgems)
#     lg = len(gems)

#     h = {}
#     for g, i in zip(sgems, range(all_types)):
#         h[g] = i
#     for g in range(lg):
#         gems[g] = h[gems[g]]
    
#     left, right = all_types, lg
#     answer = []
    
#     curmin = right
#     while left <= right:
#         mid = (left+right) // 2
#         s, e = -1, -1
#         for i in range(lg-mid+1):
#             if len(set(gems[i:i+mid])) >= all_types:
#                 s, e = i+1, i+mid
#                 break
#         if s+e == -2:
#             left = mid +1
#         else:
#             right = mid -1
#             if curmin >= mid:
#                 curmin = mid
#                 answer = [s,e]

#     return answer