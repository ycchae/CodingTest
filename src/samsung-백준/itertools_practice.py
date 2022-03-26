# https://blog.naver.com/kmh03214/221685090465

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + next


def combinations_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:], r - 1):
                yield [arr[i]] + next

# https://juhee-maeng.tistory.com/91
def permutations(array, r):
    if type(array) == type(range(0)): array = list(array)
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i] + array[i + 1:], r - 1):
                yield [array[i]] + next


def product(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr, r - 1):
                yield [arr[i]] + next

# https://blog.naver.com/kmh03214/221702095617
def powerset(s):
    masks = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss, mask in zip(s, masks) if mask & i]
