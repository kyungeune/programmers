def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)
    
    def DFS(idx, k):
        nonlocal answer
        
        if answer < idx:  # 현재가 최대 바퀴면 answer 저장
            answer = idx
        
        for i in range(len(dungeons)):
            if visited[i] == 1:
                continue
            p, c = dungeons[i]
            if k < p:
                continue
            
            visited[i] = 1
            DFS(idx+1, k-c)
            visited[i] = 0  # 백트래킹(되돌리기)
        
            
    DFS(0, k)

    return answer