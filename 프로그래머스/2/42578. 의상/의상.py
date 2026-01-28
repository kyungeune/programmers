def solution(clothes):
    cnt = {}  # 딕셔너리에 저장 ex. {"headgear": 2, "eyewear": 1}
    answer = 1
    
    # 의상 종류 count
    for arr in clothes:
        if arr[1] not in cnt:
            cnt[arr[1]] = 1
        else:
            cnt[arr[1]] += 1
    
    
    for j in cnt.values():
        answer *= (j + 1)
    
    return answer - 1