def solution(N):
    result = ''
    temp = [i for i in str(N)]
    temp.sort(reverse=True)

    for i in range(len(temp)):
        result += temp[i]

    return int(result)

test = solution(92830)
print(test)
