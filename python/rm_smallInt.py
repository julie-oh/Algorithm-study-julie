def rm_small(mylist):
    ''' https://programmers.co.kr/learn/challenge_codes/121 '''
    newlist = [int(a) for a in mylist]

    minIdx = 0
    for i in range(0, len(newlist) - 1, 1):
        if newlist[minIdx] > newlist[i]:
            minIdx = i

    newlist.pop(minIdx)
    return newlist


my_list = [4, 3, 2, 1, 0, 99, 10, 1728, 29]

print("결과 {} ".format(rm_small(my_list)))