def solution(file_object):
    # read lines of text file
    lines = file_object.readlines()
    integerBox = []

    for l in lines:
        # no white-space
        arrOfLine = l.split()
        firOfLine = arrOfLine[0]
        # if length of List not 1, existed white-space
        if 1 != len(arrOfLine):
            continue
        # if + or - sign
        if firOfLine[0] in '+-':
            if not isNumber(firOfLine[1:]):
                continue
        else:
            if not isNumber(firOfLine):
                continue
        # leading zeros
        if firOfLine[0] == '0' and 1 < len(firOfLine):
            continue
        # out of range
        if (-1000000000 > int(firOfLine)) or (1000000000 < int(firOfLine)):
            continue
        integerBox.append(int(l))
    return integerBox


# determine input is a Number
def isNumber(firOfLine):
    for i in range(len(firOfLine)):
        if firOfLine[i] not in '1234567890':
            return False
    return True

    # a = solution(open('int.txt'))
    # print(a)