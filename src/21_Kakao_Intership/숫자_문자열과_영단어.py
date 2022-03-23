def solution(s):
    answer = ''

    nums = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', 
    "six":'6', "seven": '7', "eight": '8', "nine":'9'}

    t = ""
    for c in s:
        if c.isalpha():
            t += c
            if t in nums:
                answer += nums[t]
                t = ""
        else: answer += c
        
    return int(answer)