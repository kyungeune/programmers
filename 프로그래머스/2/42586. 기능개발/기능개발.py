from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    length = len(progresses)
    a = 0  # q가 100이 될때까지 도는 바퀴수: a
    
    # 맨 처음 진행
    x = progresses[0]
    while x < 100:
        a += 1
        x += speeds[0]
    q.append(1)  # 최초의 하나
    
    for i in range(1, length):
        x = progresses[i]
        b = 0  # 현재 바퀴
        
        # q가 100이 될때까지 도는 바퀴수: a
        while x < 100:
            b += 1
            x += speeds[i]
            
        if a < b:  # -> 새로 갱신
            a = b
            total = 0
            while q:
                q.pop()
                total += 1
            answer.append(total)
            q.append(1)  # len : 1
        else:  # -> 그대로 진행
            q.append(1)
    
    if q:
        total = 0
        while q:
            q.pop()
            total += 1
        answer.append(total)
        
    return answer