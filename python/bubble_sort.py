def bubble_sort(input_val):

    for i in range(len(input_val) - 1, 0, -1):
        for j in range(0, i):
            if j == len(input_val) - 1:
                return input_val
            if input_val[j] > input_val[j + 1]:
                swap(input_val, j)

    print(input_val)


def swap(list, idx):
    if len(list) == idx - 1:
        return list

    rem = list[idx]
    list[idx] = list[idx + 1]
    list[idx + 1] = rem


if __name__ == "__main__":
    bubble_sort([3,2,1,5,9,11,20,23,11,2,1,222,111])