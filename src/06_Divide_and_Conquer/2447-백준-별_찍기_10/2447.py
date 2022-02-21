import sys; sys.setrecursionlimit(10**6)
def make_star(n):
    if n == 1: return ['*']
    stars = make_star(n//3)
    board = []
    for s in stars: board.append(s*3) 
    for s in stars: board.append(s+' '*(n//3)+s)
    for s in stars: board.append(s*3)
    return board
print('\n'.join(make_star(int(sys.stdin.readline()))))
