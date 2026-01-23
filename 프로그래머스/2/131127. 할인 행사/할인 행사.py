def solution(want, number, discount):
    answer = 0
    d = dict(zip(want, number))
    day = 0
    
    for i in discount:
        if i in d:
            d[i] -= 1
        
        if day >= 9:
            if all(v <= 0 for v in d.values()):
                answer += 1
        
            out_item = discount[day - 9]
            if out_item in d:
                d[out_item] += 1  # day가 0부터 시작하기 때문
            
        day += 1
    
    return answer