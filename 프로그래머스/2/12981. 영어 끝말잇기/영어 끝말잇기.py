def solution(n, words):
    answer = [0, 0]
    last = words[0][0]  # 마지막 글자 저장
    i = 0  # words의 idx
    wheel = 0  # 몇 바퀴인지

    while i < len(words):
        j = 0  # 몇 번째 사람인지
        wheel += 1
        
        while j < n:
            if words[i][0] != last:  # 끝난 단어로 시작하지 않으면
                return [j + 1, wheel]
            if words[i] in words[:i]:  # 말했던 단어를 또 말하면
                return [j + 1, wheel]
            
            last = words[i][len(words[i]) - 1]
            
            j += 1
            i += 1

    return answer