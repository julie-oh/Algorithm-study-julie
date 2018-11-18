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
    bubble([2, 3, 1, 10, 192, 191, 29, 21])