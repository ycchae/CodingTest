import math
k = int(input())



# def dc(k):
#     if k == 1: return 0
#     elif k == 0: return 1

#     dc(k - 2 ** int(math.log(k, 2)))

# print(dc(k))

if k == 1: print(0); exit(0)
if k == 2: print(1); exit(0)

count = 0
while True:
    # check = math.log(k, 2)
    # if check.is_integer() and check > 1:
    #     print("incheck")
    #     if count %2 == 0: print(0); exit(0)
    #     else: print(1); exit(0)

    if k == 2:
        if count %2 == 0: print(1); break
        if count %2 != 0: print(0); break
    elif k == 1 or k == 0: 
        if count %2 == 0: print(0); break
        if count %2 != 0: print(1); break

    k = k - 2 ** int(math.log(k, 2))
    count += 1
    print('k', k, count)
