N, M = map(int, input().split())
from itertools import permutations
print('\n'.join(map(' '.join, permutations(list(map(str, range(1,N+1))), M))))