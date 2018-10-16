def getLand(list):
    sumVal = 0
    for i in range(0, len(list)):
        indexNum = 0
        loofBigVal = 0
        for j in range(0, len(list[i])):
            if loofBigVal == 0:
                loofBigVal = list[i][j]
                indexNum = j
            else:
                if loofBigVal < list[i][j] and j != indexNum:
                    loofBigVal = list[i][j]
                    indexNum = j
        sumVal += loofBigVal

    print(sumVal)

if __name__ == '__main__':
    getLand([[1,2,3,5],[5,6,7,8],[4,3,2,1]])