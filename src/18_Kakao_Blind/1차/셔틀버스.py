def get_time_min(time):
    h, m = map(int, time.split(':'))
    return h*60 + m
def min_to_str(min):
    h, m = min // 60, min % 60
    hs = f"0{h}" if h < 10 else str(h)
    ms = f"0{m}" if m < 10 else str(m)
    return f"{hs}:{ms}"

def solution(n, t, m, timetable):
    answer = ''
    base = get_time_min("09:00")
    buses = [base + t*i for i in range(n)]
    max_board = m*n
    lp = len(timetable)
    times = [get_time_min(t) for t in timetable]
    times.sort()

    i = 0
    for b, bus in enumerate(buses):
        onboard = 0
        while i < lp and times[i] <= bus and onboard < m:
            onboard += 1
            i += 1
        
        # 사람 초과
        if i >= max_board: return min_to_str(times[i-1]-1)
        # 마지막 버스
        if b+1 == n:
            if onboard == m: return min_to_str(times[i-1]-1)
            return min_to_str(bus) 

    return answer

# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
print(solution(2,10,2,["09:10", "09:09", "08:00"]))