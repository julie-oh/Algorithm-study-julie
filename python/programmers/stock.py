"""
programmers problems no
42584
"""


def solution(prices):
    answer = []

    for i, p in enumerate(prices):
        if i == len(prices) - 1:
            answer.append(0)
            break

        turn = 0
        for j in range(i + 1, len(prices)):
            compare_p = prices[j]
            turn += 1

            if p <= compare_p:
                continue
            elif p > compare_p:
                break

        answer.append(turn)

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
    # [4, 3, 1, 1, 0]
