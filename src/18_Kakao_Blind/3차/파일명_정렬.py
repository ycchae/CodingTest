import re
pt = re.compile('([^\d]+)(\d{1,5})(.*)')

import heapq
def solution(files):
    heap = []
    for i, file in enumerate(files):
        head, num, _ = pt.findall(file)[0]
        head = head.lower()
        num = int(num)
        heapq.heappush(heap, (head, num, i, file))
    
    answer = [e[-1] for e in heapq.nsmallest(len(files), heap)]
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))