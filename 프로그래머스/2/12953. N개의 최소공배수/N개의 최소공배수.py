def solution(arr):
    a = arr[0]
    
    for i in range(len(arr) - 1):
        b = arr[i+1]
        
        x, y = a, b  # 최소공배수 구하기
        while y != 0:
            x, y = y, x % y
        
        a = a * b // x
    
    return a