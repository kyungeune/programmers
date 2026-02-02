def solution(n):
    answer = 0
    arr = [-1] * n

    def dfs(row):
        nonlocal answer

        if row == n:
            answer += 1
            return

        for col in range(n):
            ok = True
            for prev in range(row):
                if arr[prev] == col or abs(row - prev) == abs(col - arr[prev]):
                    ok = False
                    break

            if ok:
                arr[row] = col
                dfs(row + 1)

    dfs(0)
    return answer
