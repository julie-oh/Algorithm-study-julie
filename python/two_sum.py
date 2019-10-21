def two_sum(arr, target):
    d = {}
    index1 = 0
    index2 = 0

    for i in range(len(arr)):
        v = arr[i]
        t = target - v
        if t in d:
            index1 = i
            index2 = d[t]
            break
        else:
            d[v] = i

    return index1, index2


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))