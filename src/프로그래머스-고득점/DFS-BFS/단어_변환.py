def solution(begin, target, words):
    answer = 0
    if target not in words: return answer
    visited = [len(words)]*len(words)
    from collections import deque
    dq = deque([(begin,0)])
    while dq:
        word, cnt = dq.popleft()
        if word == target:
            return cnt
        for j in range(len(words)):
            if words[j] == word: continue
            if visited[j] <= cnt +1: continue
            diff = 0
            for c,w in zip(word, words[j]):
                if c != w: diff += 1
            if diff == 1:
                visited[j] = cnt+1
                dq.append((words[j], cnt+1))
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
