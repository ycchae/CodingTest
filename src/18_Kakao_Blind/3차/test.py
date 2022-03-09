cur = 5
n = 2
s = ''
while cur >= n:
    s = str(cur % n) + s
    cur = cur // n
s = str(cur) + s
print(s)