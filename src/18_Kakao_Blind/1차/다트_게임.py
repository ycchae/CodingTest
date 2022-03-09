import re
def solution(dartResult):
    sdt = {"S":1, "D":2, "T":3}
    pt = re.compile('(\d+)([SDT])([*#]?)')
    stack = []
    for t in pt.findall(dartResult):
        score, option = int(t[0]) ** sdt[t[1]], t[2]
        if option == '*': 
            if stack: stack.append(stack.pop()*2)
            stack.append(score*2)
        elif option == '#': stack.append(-score)
        else: stack.append(score)
    return sum(stack)

# print(solution("1S2D*3T"))
# print(solution("1D2S#10S"))
print(solution("1D2S3T*"))