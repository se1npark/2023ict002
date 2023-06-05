num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())

import statistics
data = [num1,num2,num3,num4,num5]
joong= statistics.median(data)

print((num1+num2+num3+num4+num5)//5)
print(joong)