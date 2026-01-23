from collections import deque

def solution(elements):
    answer = 0
    q = deque()
    s = set()  # s.add()
    
    for i in elements:
        q.append(i)
    
    for j in range(len(elements)):
        sum = 0
        for i in q:
            sum += i
            s.add(sum)
            
        # 순서 바꾸기
        x = q.popleft()
        q.append(x)
    
    return len(s)