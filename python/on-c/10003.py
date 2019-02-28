def play(arr):
    s = set()

    for idx, i in enumerate(arr):
        for j in range(0, len(i)):
            if i[j] == '1':
                for k in range(0, len(arr[j])):
                    if arr[j][k] == '1':
                            if arr[k][idx] == '1':
                                # sorted
                                # sort_list = [idx, j, k]
                                # sort_list.sort()
                                # s.add((sort_list[0], sort_list[1], sort_list[2]))
                                s.add(idx, j, k)

    return len(s)

if __name__ == '__main__':
    print(play(["-10","0-1","10-"])) # 3
    print(play( ["-1","0-"])) # 0