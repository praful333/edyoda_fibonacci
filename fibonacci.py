#fibonacci series
#0,1,1,2,3,5,8,13,21,34

num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(2,10):
    sum=num1+num2
    print(sum)
    num1=num2
    num2=sum