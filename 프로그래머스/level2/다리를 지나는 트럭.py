from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    tmp_truck = deque([0] * bridge_length)
    timer = 0
    sum_truck = 0
    while tmp_truck:
        timer += 1
        sum_truck -= tmp_truck.popleft()

        if truck_weights:
            if sum_truck + truck_weights[0] <= weight:
                pop_truck = truck_weights.popleft()
                tmp_truck.append(pop_truck)
                sum_truck += pop_truck
            else:
                tmp_truck.append(0)
    return timer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
