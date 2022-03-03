def solution(prices):
    plen = len(prices)
    answer = [ i for i in range (plen - 1, -1, -1)]
    stack = [0]
    for i in range (1, plen):
        print(stack)
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            print(j)
            answer[j] = i - j
        stack.append(i)
    return answer
print(solution([1,2,3,2,3]))