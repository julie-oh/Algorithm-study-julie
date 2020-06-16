def solution(clothes):
    # answer = 0
    dic = {}

    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1

    lis = []
    for d in dic:
        lis.append(dic[d] + 1)

    t = 1
    for l in lis:
       t = t * l

    return t - 1


