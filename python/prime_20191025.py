def prime(n):
    l = [i for i in range(3, n+1) if i % 2 != 0]
    p = [2]

    for i, v in l:
        p.append(v)
        d = set()
        for j in range(i+1, len(l)):
            q = l[j]
            if q % j == 0:
                d.add(q)


if __name__ == '__main__':
    print(prime(15))
