def count(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            t = i + j
            if (t == 0 or t % 2 == 0) and arr[i][j] == 'F':
                count += 1

    return count

if __name__ == '__main__':
    print(count(["........","..F.....",".....F..",".....F..","........","........",".......F",".F......"]))
    print(count(["...F....","F.......","..F.....","........","..F.....",".....F..",".F......","......F."]))