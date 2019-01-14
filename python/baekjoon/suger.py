def stage(n):
    list = [None for _ in range(0, n+1)]
    print(list)
    r = min(suger(n-5, list), suger(n-3, list))
    print(r)
def suger(n, list):
    print(n, list)
    if n == 0:
        return 0
    if n < 0:
        return False
    

if __name__ == '__main__':
    print(stage(11))