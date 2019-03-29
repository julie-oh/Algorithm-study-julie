def generator(n):
    i = 0

    while i < n:

        yield i
        i += 1

    return i

for x in generator(5):
    print(x)


if __name__ == '__main__':
    print(generator(5))