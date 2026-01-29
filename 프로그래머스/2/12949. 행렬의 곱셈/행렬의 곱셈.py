def solution(arr1, arr2):
    result = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for t in range(len(arr2)):
                result[i][j] += arr1[i][t] * arr2[t][j]

    return result