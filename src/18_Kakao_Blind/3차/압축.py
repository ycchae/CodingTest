def solution(msg):
    answer = []
    index = {}
    base = ord('A')
    for i in range(26): index[chr(base+i)] = i+1

    cur_num = 27
    max_len = 1
    lmsg = len(msg)
    i = 0
    while i < lmsg:
        target = msg[i]

        j = max_len
        while j > 1:
            if lmsg < i+j: j-=1; continue
            test = msg[i:i+j]
            if test in index: target = test; break
            j -= 1

        if i+j+1 < lmsg:
            new = msg[i:i+j+1]
            if new not in index:
                index[new] = cur_num
                cur_num += 1
                if max_len < j+1: max_len = j+1
        
        answer.append(index[target])
        i += j
    
    return answer


# print(solution("KAKAO"))
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# print(solution("ABABABABABABABAB"))
# print(solution("THATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITISTHATTHATISISTHATTHATISNOTISNOTISTHATITITIS"))

# 다른 사람 코드
# def solution(msg):
#     answer = []
#     tmp = {chr(e + ord('A')-1): e for e in range(1, 27)}
#     num = 27
#     while msg:
#         tt = 1
#         while msg[:tt] in tmp and tt <= len(msg): tt += 1
#         tt -= 1
#         if msg[:tt] in tmp:
#             answer.append(tmp[msg[:tt]])
#             tmp[msg[:tt + 1]] = num
#             num += 1
#         msg = msg[tt:]
#     return answer
