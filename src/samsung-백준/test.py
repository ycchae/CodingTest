# directions = [(0,1),((1,0)),(0,-1),(-1,0)]

# d = 0
# d = (d +5) % 4
# print(directions[d])

# from functools import reduce
# r = reduce(lambda acc, cur: acc + cur, [1,2,3], 0)
# print(r)

# right left north south
ds = [(0,1),(0,-1),(-1,0),(1,0)]
dice = [[-1,2,-1],[4,1,3],[-1,5,-1],[-1,6,-1]]
dice_bot = (3,1)
print(dice[3][1])

m = 3
print(ds[m])
dx = (dice_bot[0] - ds[m][0]) % 4
print(dice[dx][1])
dice_bot = (dx,1)

m = 0
print(ds[m])
dy = (dice_bot[1] + ds[m][1]) % 3
print(dice[1][dy])
dice_bot = (dx,dy)

m = 0
print(ds[m])
dy = (dice_bot[1] + ds[m][1]) % 3
print(dice[1][dy])
dice_bot = (dx,dy)
