def solution(office, k):
    loop_cnt = len(office) - k + 1

    compare_val = 0

    for i in range(loop_cnt):
        for j in range(loop_cnt):
            val = 0
            for n in range(k):
                for m in range(k):
                    val += office[i + n][j + m]

            if compare_val < val:
                compare_val = val

    return compare_val

if __name__ == '__main__':
    print(solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]], 2))

#arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1]