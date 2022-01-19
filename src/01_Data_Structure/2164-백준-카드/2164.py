from collections import deque

N = int(input())

cards = deque()

if N % 2 != 0:
    cards.append(N)

for i in range(2, N+1, 2):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    cards.rotate(-1)

print(cards.pop())