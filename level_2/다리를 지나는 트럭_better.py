# on_bridge 리스트에서 반복문을 돌면서 time + 1 을 해주는 것보다 훨씬 효율적임

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    on_bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    time = 0

    while truck_weights:
        total_weight -= on_bridge.popleft()
        if total_weight + truck_weights[0] > weight:
            on_bridge.append(0)
        else:
            truck = truck_weights.popleft()
            on_bridge.append(truck)
            total_weight += truck
        time += 1

    time += bridge_length

    return time