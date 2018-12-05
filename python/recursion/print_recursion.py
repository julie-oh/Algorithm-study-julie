"""
    print 1 to N using recursion
"""

def print_recursion1(n):
    for i in range(1, n+1):
        print(i)

def print_recursion2(n, arr):
    # print(11 - n)

    # append for remember
    arr.append(n)

    if n == 1:
        for i in range(len(arr) - 1, -1, -1):
            print(arr[i])

        return n

    return print_recursion2(n - 1, arr)


def print_recursion3(n):
    if n == 0:
        return n

    print_recursion3(n - 1)
    print(n)

if __name__ == '__main__':
    print_recursion2(10, arr=[])
    print_recursion3(10)