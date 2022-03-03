def solution(clothes):
    answer = 0
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for _, kind in clothes])
    print(cnt)
    answer = reduce(lambda acc, cur: acc * (cur+1), cnt.values(), 1) -1
    return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])