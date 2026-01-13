def solution(people, limit):
    answer = 0
    i = 0
    j = len(people) - 1

    # 무게가 많은 사람들부터 순차적으로 내보내야 하므로
    people.sort()
    
    while(i < j):
        if people[i] + people[j] <= limit:  # 무게의 합이 limit보다 작으면
            i += 1
            j -= 1
        else:
            j -= 1
            
        answer += 1  # 보트 하나
        
    # 한 명만 남은 경우
    if i == j:
        answer += 1
        
    return answer