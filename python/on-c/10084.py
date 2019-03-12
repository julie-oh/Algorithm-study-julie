# input value(weights, mawWeight)

def book(arr, mw):
    total = 0
    weight = 0

    for i, v in enumerate(arr):
        if i == 0:
            total = 1

        if weight + v > mw:
            total += 1
            weight = v
        else:
            weight += v


    return total

if __name__ == '__main__':
    print(book([1,1,1,7,7,7], 8)) # 4
    print(book([1], 1)) # 1
    print(book([1,15,1,15,1,15,1,15,1,15], 15)) # 10
    print(book([], 1)) # 0
    print(book([5,5,5,5,5,5], 10)) # 3
