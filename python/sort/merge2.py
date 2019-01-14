def merge_sort(arr):
    if len(arr) <= 2:
        if len(arr) == 2 and arr[1] < arr[0]:
            swap(arr, 0, 1)

        return arr
    else:
        p = len(arr) // 2
        return merge(merge_sort(arr[:p]), merge_sort(arr[p:]))

def merge(arr_1, arr_2):
    merge_arr = []
    p1 = 0
    p2 = 0

    print(arr_1, arr_2)
    a =0
   # print(arr_1, arr_2)
    while not (len(arr_1) == p1 or len(arr_2) == p2):
       if arr_1[p1] < arr_2[p2]:
           merge_arr.append(arr_1[p1])
           p1 += 1
       else:
           merge_arr.append(arr_2[p2])
           p2 += 1

       if len(arr_1) == p1:
           merge_arr += arr_2[p2:]
       elif len(arr_2) == p2:
           merge_arr += arr_1[p1:]

       a += 1


    return merge_arr


def swap(arr, idx1, idx2):
    rem = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = rem

    return arr

if __name__ == '__main__':
    print(merge_sort([2,3,1,5,2,4]))




