def solution(price, money):
    answer = 0
    sum = 0
    for i in range(0, len(price)):
        sum+=price[i]
    if sum <= money:
        answer = money-sum
    else : answer = -1
    return answer
price = list(map(int,input().split()))
money = int(input())
ret = solution(price, money)
print(ret)
