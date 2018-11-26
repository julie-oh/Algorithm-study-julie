def quicksort(arr):
    return partion(0, arr)

def partion(pivot, arr):
    pivot_val = arr[pivot]
    front = 0
    end = len(arr) - 1

    while not front == end:
        front_flag = False
        end_flag = False

        while not (front_flag and end_flag) and not (front - end == 1):
            if not front_flag:
                if arr[front] > pivot_val:
                    front_flag = True
                else:
                    front += 1

            if not end_flag:
                if arr[end] < pivot_val:
                    end_flag = True
                else:
                    end -= 1


        arr[front], arr[end] = arr[end], arr[front]

    return arr[:front], arr[front:]




if __name__ == '__main__':
    # testf_name = 'test-set/sort_test_set.txt'
    # with open(testf_name, 'r') as testf:
    #     lines = testf.readlines()
    #     for line in lines:
    #         int_arr = [int(s) for s in line.strip().split(',')]
    #         quicksort(int_arr)

    print(quicksort([5, 1, 7, 9, 3]))
# 12, 323, 1, 10, 192, 191, 29, 21
# -1, 291, 210, 11, 01, 2983, 1930