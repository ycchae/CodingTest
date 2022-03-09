def get_start_end_msec(datetime):
    time = datetime.split()[1]
    duration_msec = int(float(datetime.split()[2][:-1]) * 1000)
    h,m,s = map(float, time.split(':'))
    end_msec = int(3600*h *1000)
    end_msec += int(60*m *1000)
    end_msec += int(s *1000)
    start_msec = end_msec - duration_msec +1
    return (start_msec, end_msec)

def solution(lines):
    answer = 0
    ll = len(lines)
    times = [get_start_end_msec(line) for line in lines]
    for i in range(ll):
        cnt = 1
        for j in range(i+1, ll):
            if times[j][0] < times[i][1] + 1000: cnt += 1
        if answer < cnt: answer = cnt

    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s","2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s","2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s","2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s","2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]))