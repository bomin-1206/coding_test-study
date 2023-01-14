answer = [1, 1, 2, 2, 2, 8]
count = [0]*6
arr = list(map(int, input().split()))
for i in range(0, len(arr)):
    if arr[i] != answer[i]:
        count[i] = answer[i] - arr[i]
for i in range(0, len(arr)):
    print(count[i], end = " ")
