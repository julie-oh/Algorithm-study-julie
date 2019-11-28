def solution(n, computers):
    is_connect = {i: False for i in range(n)}

    for i, computer in enumerate(computers):
        print(i, computer)
        for j, v in enumerate(computer):
            print('=================')
            print(j, v)
            if i == j or is_connect[i] is True:
                break
            else:
                if computer[i][j] == 1 and computer[j][i] == 1:
                    n -= 1
                    is_connect[j] = True

    return n


if __name__ == '__main__':
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])