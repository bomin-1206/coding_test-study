def func_a(num):
    answer = 0
    for i in range(1, num+1):
        answer+=i
    return answer
def solution(n, m):
    sum_m = func_a(m)
    sum_n = func_a(n-1)
    return sum_m - sum_n
n = int(input())
m = int(input())
ret = solution(n, m)
print(ret)
