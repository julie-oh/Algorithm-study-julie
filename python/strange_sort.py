def strange_sort(list, n):
    ''' https://programmers.co.kr/learn/challenge_codes/95 '''

    for i in range(len(list) - 1, 0, -1):
        for j in range(0, i, 1):
            if list[j][n] > list[j + 1][n]:
                swap(list, j, j + 1)
    return list


def swap(arr, i, j):
    rem = arr[i]
    arr[i] = arr[j]
    arr[j] = rem


print(strange_sort(['efg','abc'], 1))
print(strange_sort(["yeonjoo", "julie", "apple"], 0) )