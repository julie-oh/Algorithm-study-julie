def solution(phone_book):
    answer = True
    s = set()

    for p in phone_book:
        for i in range(1, len(p)):
            s.update([p[:i]])

    for p in phone_book:
        if p in s:
            return False


    return answer