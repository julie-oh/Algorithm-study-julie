def bubble(arr):
    for i in range(len(arr) -1, 1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # swap(arr, j)

    print(arr)

def swap(arr, idx):
    rem_val = arr[idx + 1]

    arr[idx + 1] = arr[idx]
    arr[idx] = rem_val

    return arr


if __name__ == '__main__':
    test_fname = 'test-set/sort_test_set.txt'
    with open(test_fname, 'r') as testf:
        lines = testf.readlines()
        for line in lines:
            int_arr = [int(s) for s in line.strip().split(',')]
            bubble(int_arr)
