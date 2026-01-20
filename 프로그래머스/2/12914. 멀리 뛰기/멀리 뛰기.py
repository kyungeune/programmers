import math

def solution(n):
    MOD = 1234567
    a, b = 1, 2
    
    if n == 1:
        return 1
    # “한 칸 앞으로 이동한다
    # 이전 값은 버리고
    # 새 dp 값을 계산해서 갱신한다”  
    
    for i in range(3, n + 1):
        a, b = b, (a + b) % MOD
    
    return b