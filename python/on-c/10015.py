def max_num(l, h):
    dic = set([0])
    p = 1
    while True:
        n = p*p

        if n > h:
            break

        dic.add(p*p)
        p += 1

    # duplicate case

    print(dic)




if __name__ == '__main__':
    print(max_num(0,2)) #2
    # print(max_num(0, 30))  # 25
    # print(max_num(0, 0))  # 0
    # print(max_num(100, 101))  # 100
    # print(max_num(5, 99))  # 85