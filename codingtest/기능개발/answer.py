# 틀린 문제 (한 가지 예시만을 통과하지 못함)

def solution(progresses, speeds):
    
    count = 1
    due_date = []
    result = []
    prev = 0
    for p, s in zip(progresses, speeds):
        due_date.append((100 - p) // s)
        print(due_date)
        
    for term in due_date:
        if prev == 0:
            prev = term
        
        elif prev >= term:
            count += 1
        
            
        elif prev < term:
            result.append(count)
            count = 1
            prev = term
            
    result.append(count)
        
    
    return result
