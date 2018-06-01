''' https://programmers.co.kr/learn/courses/30/lessons/12945 '''
def fibonacci(n):
    remArr = [1, 1]

    for _ in range(2, n):
        fibVal = remArr[-1] + remArr[-2]

        if fibVal >= 1234567:
            remArr.append(fibVal - 1234567)
        else:
            remArr.append(fibVal)

    print(remArr)
    return remArr[-1]

if __name__ == '__main__':
    fibonacci(3)