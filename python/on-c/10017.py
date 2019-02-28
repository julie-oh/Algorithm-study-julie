def prime(n):
    s = set(range(2,n))

    for j in range(2, n):
        remove_val = []
        for i, v in enumerate(s):
            if not v == j and v % j == 0:
                remove_val.append(v)

        if len(remove_val) > 0:
            for i in range(0, len(remove_val)):
                s.remove(remove_val[i])


    # for i in range(0, len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[j] % arr[i] == 0:
    #             remove_val.add(arr[j])
    #
    # for i, v in enumerate(remove_val):
    #     s.remove(v)

    square = set()

    if n < 2:
        return 0

    for i, v in enumerate(s):
        reminder = n - v
        if reminder in s:
            arr = [v, reminder]
            arr.sort()
            square.add(tuple(arr))

    return len(square)


if __name__ == '__main__':
    import timeit

    print(prime(10)) # 2
    print(prime(4)) # 1
    print(prime(6))  # 1
    print(prime(10))  # 2
    print(prime(648))  # 27
    import time
    start_time = time.time()
    print(prime(3570))  # 154
    end_time = time.time()
    print(end_time - start_time)



