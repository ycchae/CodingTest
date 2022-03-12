def solution(record):
    order = []
    nicks = {}
    for r in record:
        
        sp = r.split()
        cmd = sp[0]
        id = sp[1]
        if cmd != 'Change': order.append((cmd, id))
        if cmd != 'Leave': nicks[id] = sp[2]

    answer = []
    for o in order:
        if o[0] == 'Enter': answer.append(f"{nicks[o[1]]}님이 들어왔습니다.")
        elif o[0] == 'Leave': answer.append(f"{nicks[o[1]]}님이 나갔습니다.")
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))