def king(w, l):
    arr = [[False] * 6 for i in range(4)]
    key = [(1,0), (0,1), (-1, 0), (0, -1)]
    curr = (len(arr)-1, 0)

    while True:
        # if
        # arr[curr[0]][curr[0]] = True

if __name__ == '__main__':
    print(king(6, 4))