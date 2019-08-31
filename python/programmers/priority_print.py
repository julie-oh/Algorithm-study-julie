"""
    https://programmers.co.kr/learn/courses/30/lessons/42587
"""

def solution(p, l):
    ans = 0
    m = max(p)

    while True:
        v = p.pop(0)

        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p) - 1
            else:
                l -= 1
    print(ans)
    return ans


if __name__ == '__main__':
    solution([1, 1, 9, 1, 1, 1], 0)

