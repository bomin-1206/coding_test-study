def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer
height = list(map(int, input().split()))
k = int(input())
ret = solution(height, k)
print(ret)
