def solution(estimates, k):
    l_cnt = (len(estimates) - k) + 1

    re = 0
    rem = 0
    for i in range(l_cnt):
        if i == 0:
            sum_val = sum(estimates[i:k])
            re = sum_val
        else:
            sum_val = rem + estimates[i+(k-1)]
            if sum_val > re:
                re = sum_val

        rem = sum_val - estimates[i]

    return re


if __name__ == '__main__':
    print(solution([1, 1, 9, 3, 7, 6, 5, 10], 4))