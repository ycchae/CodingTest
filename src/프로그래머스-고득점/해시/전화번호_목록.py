def solution(phone_book):
    hash_map = {}
    for pn in phone_book:
        hash_map[pn] = 1
    for pn in phone_book:
        prefix = ""
        for number in pn:
            prefix += number
            if prefix in hash_map and prefix != pn:
                return False
    return True