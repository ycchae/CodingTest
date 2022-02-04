N = int(input())
b = 0
while N >= 0:
    if N % 5 == 0:
        b += N // 5
        print(b)
        break
    N -= 3
    b += 1
else:
    print(-1)