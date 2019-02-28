def finger(wFinger, maxCnt):
    total_cnt = 0
    week_cnt = 0
    point = 1
    is_plus = True

    while True:
        if point == wFinger:
            week_cnt += 1
            if week_cnt > maxCnt:
                break

        total_cnt += 1

        if point == 5:
            is_plus = False
        if point == 1:
            is_plus = True

        if is_plus:
            point += 1
        else:
            point -= 1


    return total_cnt

if __name__ == '__main__':
    print(finger(2, 3))
    print(finger(2, 48))