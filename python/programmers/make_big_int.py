"""https://programmers.co.kr/learn/courses/30/lessons/42883"""

def solution(number, k):
    n_list = [i for i in number]
    n_list.sort(reverse=True)

    a = ''.join(str(n_list[i]) for i in range(0, len(n_list)-k))

    return a

if __name__ == '__main__':
    print(solution("4177252841", 4)) # 775841