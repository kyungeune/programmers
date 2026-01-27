def solution(citations):
    citations.sort()
    i = 0  # 현재 인덱스
    
    while i < len(citations):
        x = citations[i]  # 현재 인덱스에 들어있는 "숫자"
        h = len(citations) - i  # 뒤쪽 인용 횟수
        
        if x >= h:  # 처음으로 통과한 게 가장 큰 값
            return h
        
        i += 1  # 하나씩 커지게 이동
    
    return 0