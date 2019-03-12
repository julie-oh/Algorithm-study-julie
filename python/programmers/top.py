"""
    programmers problems
    (https://programmers.co.kr/learn/courses/30/lessons/42588?language=python3)
"""
def solution(arr):
    re_arr = [0 for _ in range(0, len(arr))]

    for i in range(len(arr)-1, 0, -1):
        spot = arr[i]
        for j in range(i-1, -1, -1):
            if spot < arr[j]:
                re_arr[i] = j+1
                break

    return re_arr

if __name__ == '__main__':
    print(solution([6,9,5,7,4])) # [0,0,2,2,4]
    print(solution([3,9,9,3,5,7,2]	))  # [0,0,0,3,3,3,6]
    print(solution([1,5,3,6,7,6,5]	))  # [0,0,2,0,0,5,6]
