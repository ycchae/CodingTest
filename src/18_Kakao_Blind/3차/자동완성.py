def solution(words):
    answer = 0
    head = dict()

    for word in words:
        cur = head
        for c in word:
            if c not in cur: cur[c] = {}
            cur = cur[c]
        cur['*'] = True

    for word in words:
        lw = len(word)
        cur = head
        boundary = 0
        for i, c in enumerate(word):
            if len(cur) > 1: boundary = i
            cur = cur[c]
        if len(cur) > 1: boundary = i

        if boundary == lw-1: answer += lw
        else: answer += boundary + 1

    return answer

# print(solution(["go","gone","guild"]))
# print(solution(["abc","def","ghi","jklm"]))
print(solution(["word", "war", "warrior", "world"]))