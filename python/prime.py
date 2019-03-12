import math

def prime(n):
    # set in 2 to n numbers
    num = set(range(2, n+1))

    for i in range(2, int(math.sqrt(n))+1):
        remove_arr = []

        for n in num:
            if not i == n and n % i == 0:
                remove_arr.append(n)

        for r in remove_arr:
            num.remove(r)

    return len(num)



if __name__ == '__main__':
    print(prime(1000))