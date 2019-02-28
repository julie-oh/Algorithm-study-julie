def fib(n):
    arr_0 = fib_helper_0(n, [None] * (n+1))
    arr_1 = fib_helper_1(n, [None] * (n+1))

    return [arr_0, arr_1]

def fib_helper_0(n, arr):
    if n == 0:
        return 1

    if n == 1:
        return 0

    if arr[n] is not None:
        return arr[n]

    arr[n] = fib_helper_0(n-1, arr) + fib_helper_0(n-2, arr)
    return arr[n]


def fib_helper_1(n, arr):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if arr[n] is not None:
        return arr[n]

    arr[n] = fib_helper_1(n - 1, arr) + fib_helper_1(n - 2, arr)
    return arr[n]


if __name__ == '__main__':
    print(fib(4))
    print(fib(0))
    print(fib(40))