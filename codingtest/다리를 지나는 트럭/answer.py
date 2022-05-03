# 시간 초과 ... (슬라이딩 윈도우 참조할 것)
2, 10, [7, 4, 5, 6] [0, 0, 0, 6]
def solution(bridge_length, weight, truck_weights):
    bridge = truck_weights[:1]
    truck_weights = truck_weights[1:]
    time = 1
    while sum(bridge) != 0:
        if len(bridge) == bridge_length: # 다리 length가 꽉 찼다면
            bridge.pop(0) # 다리의 0번 인덱스는 내린다.

            if len(truck_weights) != 0: # 트럭 리스트에 요소가 남아있다면
                if sum(bridge) + truck_weights[0] <= weight: # 지금 다리 중량에 트럭이 더 타도 되면
                    bridge.append(truck_weights.pop(0)) # 더 태운다
                    
                else: # 중량 초과면
                    bridge.append(0) # 0을 태운다.

            else: # 트럭 리스트에 요소가 없다면
                    bridge.append(0) # 0을 태운다.
            
        else: # 다리 자리가 남아있다면

            if len(truck_weights) != 0: # 트럭 리스트에 요소가 남아있다면
                if sum(bridge) + truck_weights[0] <= weight: # 지금 다리 중량에 트럭이 더 타도 되면
                    bridge.append(truck_weights.pop(0)) # 더 태운다
                    
                else: # 중량 초과면
                    bridge.append(0) # 0을 태운다.

            else: # 트럭 리스트에 요소가 없다면
                bridge.append(0) # 0을 태운다.
        
        time += 1
        
    return time
