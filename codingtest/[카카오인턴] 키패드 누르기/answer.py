def tuple_cal(tuple1, tuple2):
    return (abs(tuple1[0] - tuple2[0]), abs(tuple1[1] - tuple2[1]))

def solution(numbers, hand):
    loc = {
        1: (0, 0), 2: (0, 1), 3: (0, 2), 
        4: (1, 0), 5: (1, 1), 6: (1, 2), 
        7: (2, 0), 8: (2, 1), 9: (2, 2), 
        "L": (3, 0), 0: (3, 1), "R": (3, 2)
    }
        
    l_thumb, r_thumb = "L", "R"
    result = ""
    
    for i in numbers:
        if loc[i][1] == 0:
            result += "L"
            l_thumb = i
        elif loc[i][1] == 2:
            result += "R"
            r_thumb = i
        elif loc[i][1] == 1:
            left = tuple_cal(loc[l_thumb], loc[i])
            right = tuple_cal(loc[r_thumb], loc[i])      
            if (left < right) & (sum(left) != sum(right)):
                result += "L"
                l_thumb = i
            elif sum(left) == sum(right):
                result += hand[0].upper()
                if hand == 'left':
                    l_thumb = i
                else:
                    r_thumb = i

            else:
                result += "R"
                r_thumb = i
                
    return result
