def sell(p, d):
    rem = 0
    total = 0

    for i in range(0, len(p)):
        pick = p[i]
        total_r = 0

        for j in range(0, len(p)):
            if pick > p[j] or pick < d[j]:
                continue

            total_r += p[j] - d[j]

        if total < total_r:
            total = total_r
            rem = pick


    return rem




if __name__ == '__main__':
    print(sell([13,22,35], [5,15,30])) # 13
    print(sell([13, 22, 35], [15,30,40]))  # 0
    print(sell([10,10,20,20,5], [1,5,11,15,0]))  # 10
    print(sell( [13,17,14,30,19,17,55,16], [12,1,5,10,3,2,40,19]))  # 17
