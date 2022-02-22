import sys
for i in sys.stdin:
    s = '-'
    for j in range(int(i)):
        s = s + " "*len(s) + s
    print(s)