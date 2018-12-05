"""
    square N using recursion
"""

def square1(power):
    re = 2

    if power == 1:
        return re

    for i in range(2, power+1):
        re = re * 2

    print(re)

def square2(n, power):
    if power == 1:
        return n

    return n * square2(n, power - 1)


if __name__ == '__main__':
    print(square2(2, 10))