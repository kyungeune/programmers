import math

def solution(n,a,b):
    nextNum = 1  # 다음 대결의 승자 개수
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    
    while nextNum > 0:
        if a == b | (a == 1 and b == 2) | (a == 2 and b == 1):
            return nextNum
        else:
            nextNum += 1
            
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        
    return nextNum