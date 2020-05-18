"""
programmers problems no
42583
"""


from collections import deque

sum_truck_in_bridge = 0


def left_move(q):
    global sum_truck_in_bridge

    p = q.popleft()
    sum_truck_in_bridge -= p
    q.append(0)
    return q


def solution(bridge_length, weight, truck_weights):
    global sum_truck_in_bridge
    answer = 0

    q = deque(0 for _ in range(0, bridge_length))
    point = 0

    while True:
        if point >= len(truck_weights):
            while sum_truck_in_bridge > 0:
                q = left_move(q)
                answer += 1
            else:
                break

        answer += 1
        truck_weight = truck_weights[point]

        if point == 0:
            q.pop()
            q.append(truck_weight)
            sum_truck_in_bridge += truck_weight
            point += 1
            continue

        q = left_move(q)

        current_weight = sum_truck_in_bridge

        if current_weight + truck_weight <= weight and q[-1] == 0:
            q[-1] = truck_weight
            sum_truck_in_bridge += truck_weight
            point += 1

    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))  # 8
    print(solution(100, 100, [10]))  # 101
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110

