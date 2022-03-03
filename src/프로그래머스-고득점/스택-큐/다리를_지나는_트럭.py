def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on = [0] * bridge_length
    while len(trucks_on):
        answer += 1
        trucks_on.pop(0)
        if truck_weights:
            if sum(trucks_on) + truck_weights[0] <= weight:
                trucks_on.append(truck_weights.pop(0))
            else:
                trucks_on.append(0)
    return answer
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))

