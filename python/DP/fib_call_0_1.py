""" return count(Int) that count calls for fib(0) or fib(1)"""

def fib(n):
    return fib_helper(n, [None] * (n+1))


def fib_helper(n, arr_0):
    if n == 0:
        return 1
    if n == 1:
        return 0

    if arr_0[n] is not None:
        return arr_0[n]

    arr_0[n] = fib_helper(n-1, arr_0) + fib_helper(n-2, arr_0)

    return arr_0[n]


if __name__ == '__main__':
    print(fib(4))
    print(fib(5))
    print(fib(13))