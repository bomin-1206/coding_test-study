num1 = int(input())
num2 = int(input())
num = num2
while num!=0:
    tmp = num%10
    print(num1*tmp)
    num//=10
print(num1*num2)
