from collections import defaultdict
def solution(cacheSize, cities):
    answer = 0
    cache = defaultdict(int)
    if cacheSize == 0: return len(cities) * 5

    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache: answer += 1
        else:
            answer += 5
            if len(cache) == cacheSize:
                min_val = 100_001
                min_key = 0
                for k,v in cache.items():
                    if min_val > v:
                        min_val = v
                        min_key = k
                del cache[min_key]
        cache[city] = i
    return answer

print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))