""" return count(Int) that count calls for fib(0) or fib(1)"""

def fib(n):
    return fib_helper(n, [None] * (n + 1))


def fib_helper(n, arr):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if arr[n] is not None:
        return arr[n]

    cnt =  fib_helper(n-1, arr) + fib_helper(n-2, arr)
    arr[n] = cnt
    return cnt

if __name__ == '__main__':
    print(fib(5))
    print(fib(13))