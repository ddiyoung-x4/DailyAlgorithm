from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = deque(truck_weights)
    on_bridge = deque()
    sum_weight = 0
    time = 0
    while True:
        time += 1
        if len(truck_weights) != 0 and sum_weight + truck_weights[0] <= weight:
            truck_info = truck_weights.popleft()
            sum_weight += truck_info
            on_bridge.append([0, truck_info])
            
        
        for i, (t, turck_info) in enumerate(on_bridge):
            on_bridge[i] = [t+1, turck_info]
        
        # print(on_bridge)
        if len(on_bridge) != 0 and on_bridge[0][0] == bridge_length:
            t, truck_info = on_bridge.popleft()
            sum_weight -= truck_info
        
        
        if len(truck_weights) == 0 and len(on_bridge) == 0:
            break
        
    answer = time +1    
        
    return answer