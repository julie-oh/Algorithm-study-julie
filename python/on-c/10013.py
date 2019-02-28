def eight(l, h):
    l = str(l)
    h = str(h)

    if not len(l) == len(h):
        return 0

    cnt = 0
    for i in range(0, len(l)):
        if l[i] == h[i]:
            cnt += 1

    return cnt

if __name__ == '__main__':
    print(eight(1, 10)) #0
    print(eight(88, 88)) #2
    print(eight(800, 899)) #1
    print(eight(8808, 8880)) #2
    print(eight(8, 88)) #0