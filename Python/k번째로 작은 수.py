def solution(arr, k):
    answer = 0
    cnt = 0
    min = 21470000
    while cnt!=k:
        for i in range(0, 4):
            for j in range(0, 4):
                if arr[i][j] < min:
                    min = arr[i][j]
                    answer = min
        cnt+=1
    return answer
arr = [[0]*4]*4
arr = list(map(int, input().split()))
k = int(input())
ret = solution(arr, k)
print(ret)
