def one_to_num(num):
    for i in range(1, num+1):
        print(i)

if __name__ == '__main__':
    num = input().strip().split()
    one_to_num(int(num))