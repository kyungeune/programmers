def solution(n, left, right):
    answer = []
    
    
    a = left // n
    b = left % n
    sum = 0
    need = right - left + 1
    
    for i in range(a, n):
        for j in range(b, n):
            if i+1 >= j+1:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
            
            sum += 1
            if sum == need:
                return answer
        b = 0
    
    
    return answer