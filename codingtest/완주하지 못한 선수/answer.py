def solution(participant, completion):
    part_dict = {}
    for name in participant:
        if name in part_dict:
            part_dict[name] += 1
        else:
            part_dict[name] = 1
    
    for j in completion:
        if part_dict[j] == 1:
            del part_dict[j]
        else:
            part_dict[j] -= 1
    
    return list(part_dict.keys())[0]
