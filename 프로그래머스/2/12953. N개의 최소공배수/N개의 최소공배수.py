def solution(arr):
    a = arr[0]
    
    for i in range(len(arr) - 1):
        b = arr[i+1]
        
        x, y = a, b  # 최대공약수 : x
        while y != 0:
            x, y = y, x % y
        
        # 두 수의 곱 / 최대공약수 = 최소공배수
        a = a * b // x
    
    return a