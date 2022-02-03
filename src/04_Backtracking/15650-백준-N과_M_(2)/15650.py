N, M = map(int, input().split())

s = []
def f():
  if len(s) == M:
    print(' '.join(map(str, s)))
    return

  for i in range(1, N + 1):
    if i in s or (len(s) > 0 and i < s[-1]):
      continue
    s.append(i)
    f()
    s.pop()

f()