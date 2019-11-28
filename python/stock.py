def stock(arr):
    if len(arr) == 0:
        return 0

    min = arr[0]
    max = None

    for i in range(1, len(arr)):
        v = arr[i]
        if v <= min:
            min = v
        else:
            if max is None and min < v:
                max = v
            elif max < v:
                max = v

    if type(min) == int and type(max) == int:
        return max - min
    else:
        return min

if __name__ == '__main__':
    print(stock([7,1,5,3,6,4]))
    print(stock([7,6,4,3,1]))