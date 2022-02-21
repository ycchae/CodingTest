import sys
input = sys.stdin.readline

d = {}
total = 0
while True:
    s = input().strip()
    if s == "": break

    if not d.get(s): d[s] = 1
    else: d[s] += 1
    total += 1

for s in sorted(list(d.keys())):
    print(f"{s} {100*(d[s]/total):.4f}")
