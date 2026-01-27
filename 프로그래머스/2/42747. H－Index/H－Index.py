def solution(citations):
    answer = 0
    citations.sort()
    i = 0
    
    while i < len(citations):
        x = citations[i]
        h = len(citations) - i
        
        # 인용되지 않은 게 x번 이하거나, 인용된 게 x번 이상
        if x >= h:
            return h
        i += 1
    
    return answer