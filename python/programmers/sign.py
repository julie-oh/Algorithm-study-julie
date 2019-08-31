def solution(phrases, second):
    total = len(phrases) + 14
    sign = ['_' for _ in range(0,total)]

    if total-second < 0:
        start = total-second % total
    else:
        start = total-second

    p_i = 0
    for i in range(start, total):
        if p_i >= len(phrases):
            break

        sign[i] = phrases[p_i]
        p_i += 1

    return ''.join(sign[len(phrases):])


if __name__ == '__main__':
    for i in range(300):
        print(solution('happy-birthday', i))