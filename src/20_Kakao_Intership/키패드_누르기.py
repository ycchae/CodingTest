def solution(numbers, hand):
    answer = ''

    def get_rc(num):
        if num == 0:
            return (3, 1)
        r = (num-1) // 3
        c = (num-1) % 3
        return (r, c)

    def get_distance(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    cur_left = (3, 0)
    cur_right = (3, 2)

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
        else:
            dl = get_distance(cur_left, get_rc(num))
            dr = get_distance(cur_right, get_rc(num))
            print(num, dl, dr)

            if dl < dr:
                answer += 'L'
            elif dr < dl:
                answer += 'R'
            else:
                answer += "R" if hand == "right" else "L"

        if answer[-1] == 'L':
            cur_left = get_rc(num)
        else:
            cur_right = get_rc(num)
            
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
