def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    s, e = 0, distance // (len(rocks)-n)
    while s <= e:
        mid = (s+e) // 2

        last_rock_pos = 0
        removed = 0
        for r in rocks:
            d = r - last_rock_pos
            if d < mid:
                removed += 1
            else:
                last_rock_pos = r

        if removed > n:
            e = mid - 1
        else:
            s = mid + 1
            answer = mid
        

    return answer

print(solution(25,[2, 14, 11, 21, 17],2))