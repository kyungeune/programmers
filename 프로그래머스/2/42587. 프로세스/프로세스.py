from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    
    # 논리 구조
    # 방금 꺼낸 게 가장 큰 수면 실행
    # location은 0부터 실행
    # 앞에서부터 돌아가며 확인하기
    
    for i in priorities:
        q.append(i)
    
    while q:
        current = q.popleft()
        
        # 맨 처음인 경우 별개 실행
        if location == 0:  
            if all(x <= current for x in q):
                answer += 1
                return answer
            else:
                q.append(current)
                location = len(q) - 1
            continue
            
        if all(x <= current for x in q):
            answer += 1
        else:
            q.append(current)
            
        print(location)
        location -= 1
        
    return answer