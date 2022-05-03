def solution(priorities, location): # 문서 중요도, 위치
    pnt = 0
    while len(priorities) != 0:
        if location == 0:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else:
                return pnt + 1
            
        else:
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location -= 1
            else: # 최대값이 0번 자리에 오면
                priorities.pop(0)
                location -= 1
                pnt += 1 # 프린트
