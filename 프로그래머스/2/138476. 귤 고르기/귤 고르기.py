def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    
    # arr에 각 몇 개 저장되어 있는지 저장
    arr = [0]*10000001
    used_idx = set()  # 중복 없이, 빠르게, 존재 여부를 확인하면서 인덱스를 모으기 위함
    
    # arr에 개수 저장
    for x in tangerine:
        arr[x] += 1
        used_idx.add(x)
    
    
    # 개수만 모으기
    gaesu = [] 
    for i in used_idx:
        gaesu.append(arr[i])
    
    gaesu.sort(reverse=True)
    
    total = 0
    for i in gaesu:
        # if i > k:
        #     continue
            
        answer+=1
        total += i
        if total >= k:
            break
    
    return answer