N, M = map(int, input().split())

numList = [i for i in range(0, N+1)]
# [0, 1, 2, 3, 4]

index = 0

def backTracking(result):

    if len(result) == M:
        print(*result)
        return

    for i in range(1, N+1):
        if (i not in result) and (len(result)==0 or i > result[-1]):
            result.append(numList[i])
            backTracking(result)
            result.pop()

backTracking([])