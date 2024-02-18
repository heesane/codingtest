from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    while bridge:
        time += 1
        passed_truck = bridge.popleft()
        bridge_weight -= passed_truck
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge_weight += next_truck
                bridge.append(next_truck)
            else:
                bridge.append(0)
    
    return time
