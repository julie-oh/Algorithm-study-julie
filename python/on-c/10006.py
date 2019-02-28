def money(arr, m):
    rem = [None] * (m + 1)
    noneset = [0] * len(arr)  # [0, 0, 0]
    rem[0] = {tuple(noneset)}  # {(0, 0, 0)}
    helper(arr, m, rem)
    # for val, comb in enumerate(rem):
    #     print('{}: {}'.format(val, comb))
    return len(rem[m])

def helper(arr, m, rem):
    # rem = combination
    if m < 0:  # impossible
        return rem

    # 이미 계산되어 있음 - 무시
    if rem[m] is not None:
        return rem

    # 현재 가격 m을 만들기 위한 모든 경우의 수를 저장
    curr_comb = set()
    for idx, val in enumerate(arr):
        val_before = m - val  # 이전 가격
        helper(arr, val_before, rem)
        if val_before  < 0:
            continue

        for counts in rem[val_before]:  # 이전 가격을 만들 수 있는 모든 경우의 수
            c_list = list(counts)
            c_list[idx] += 1  # count update  # 해당 동전의 개수를 하나 추가하고 저장
            curr_comb.add(tuple(c_list))

    rem[m] = curr_comb
    return rem



if __name__ == '__main__':
    rem  = []
    print(money([1,5,10], 10))
    print(money([4,25,40], 80))
    print(money([10, 11, 38, 39, 40, 41, 48], 55))
    print(money([1,21,24,31,35,37,47], 57))

