def solution(cacheSize, cities):
    answer = 0
    length = len(cities)
    arr = []
    
    # cacheSize가 0인 경우, pop from empty list Error 방지
    if cacheSize == 0:
        return 5 * length
        
    # Newyork과 NEWYORK을 동일하게 인식하도록 전부 대문자로 변환
    for i in range(length):
        cities[i] = cities[i].upper()
    
    # 처음 캐시크기만큼 집어넣을 때는 cities[:i]까지만 확인
    for i in range(cacheSize):
        now = cities[i]
        if now in cities[:i]:
            answer += 1
        else:
            answer += 5
        arr.append(now)
    
    
    if cacheSize >= length:
        return anwer
    
    # 이후는 캐시크기만큼씩 확인
    for i in range(cacheSize, length):
        now = cities[i]
        # 이미 arr에 존재하면
        if now in arr:
            
            # 맨 앞에꺼 빼기
            x = arr.pop(0)
            arr.append(now)
            # 만약 제외했는데도 배열에 또 있으면 뺐던건 다시 넣어주기..
            if now in arr:
                arr.insert(0, x)
                arr.remove(now)  # 앞에서부터 지워짐
            
            answer += 1
        
        # arr에 존재하지 않으면
        else:
            arr.pop(0)
            arr.append(now)
            
            answer += 5
    
    return answer