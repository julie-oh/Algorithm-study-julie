def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                print("i == " , i)
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


if __name__ == '__main__':
    print(insertion_sort([1, 2, 6, 4, 1, -6, 7, 81]))