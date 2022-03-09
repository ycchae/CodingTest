import heapq
import re
K = ["C#", "D#", "A#", "G#", "F#", "C", "D", "E", "F", "G", "A", "B"]
pt = re.compile(f"{'|'.join(K)}")

def played(start, end, song):
    sh, sm = start.split(':')
    eh, em = end.split(':')
    duration = (int(eh)*60 + int(em)) - (int(sh)*60 + int(sm))
    return song*(duration // len(song)) + song[:duration % len(song)]

def solution(m, musicinfos):
    candidates = []
    lm = pt.findall(m)
    llm = len(lm)
    for i, music in enumerate(musicinfos):
        start, end, name, song = music.split(',')
        lsong = pt.findall(song)
        lsong = played(start, end, lsong)
        llsong = len(lsong)
        for i in range(llsong - llm+1):
            if lm == lsong[i:i+llm]:
                heapq.heappush(candidates, (-len(lsong), i, name))
                break
    if candidates: return candidates[0][2]
    return "(None)"

print(solution("ABC",["12:00,12:03,HELLO,ABC", "13:00,13:01,WORLD,A"]))
# print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))