def solution(tickets):
    answer = []
    routes = {}
    for ticket in tickets:
        if not routes.get(ticket[0]):
            routes[ticket[0]] = []
        routes[ticket[0]].append(ticket[1])
    for key in routes.keys(): routes[key].sort()

    stack = ["ICN"]
    while stack:
        cur = stack[0]
        if not routes.get(cur) or not routes[cur]:
            answer.append(stack.pop(0))
        else:
            stack.insert(0, routes[cur].pop(0))
    return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "IAD"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"], ["HND", "IAD"], ["IAD", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))