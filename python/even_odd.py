def even_odd(arr):
    begin = 0
    end = len(arr) - 1
    begin_flag = False
    end_flag = False

    while begin < end:
        if begin_flag and end_flag:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin += 1
            end -= 1
            begin_flag = False
            end_flag = False

        if not begin_flag and arr[begin] % 2 == 0:
            begin += 1
        else:
            begin_flag = True

        if not end_flag and arr[end] % 2 == 1:
            end -= 1
        else:
            end_flag = True


    return arr

if __name__ == '__main__':
    print(even_odd([2,23,1,23,0,2,12,3,4]))