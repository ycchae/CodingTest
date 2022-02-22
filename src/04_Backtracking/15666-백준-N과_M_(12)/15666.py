N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
solve = []

def f(d):
  if d == M:
    print(' '.join(map(str, solve)))
    return

  for i in range(len(arr)):
    if d == 0 or solve[-1] <= arr[i]:
      solve.append(arr[i])
      f(d+1)
      solve.pop()

f(0)