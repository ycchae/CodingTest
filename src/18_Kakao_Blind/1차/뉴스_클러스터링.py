from collections import defaultdict

def solution(str1, str2):
    set1 = defaultdict(int)
    set2 = defaultdict(int)
    
    intersection = 0
    union = 0
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            key = str1[i].lower()+str1[i+1].lower()
            set1[key] += 1
            union += 1

    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            key = str2[i].lower()+str2[i+1].lower()
            set2[key] += 1
            if key not in set1: union += 1

    for key, val in set1.items():
        if set2.get(key):
            if val < set2[key]:
                intersection += val
                union += set2[key] - val
            else:
                intersection += set2[key]

    if union == 0: return 65536
    return int((intersection / union)*65536)


print(solution("FRANCE", "french"))
print(solution("aa1+aa2", "AAAA12"))