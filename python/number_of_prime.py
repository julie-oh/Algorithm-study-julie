def number_of_prime(n):
    list = [2]

    for i in range(2, n + 1):
        flag = true
        for j in range(0, len(list)):
            if i % list[j] == 0:
                flag = false
                break

        if flag:
            list.append(i)

    print list

if __name__ == '__main__':
    number_of_prime(50)
