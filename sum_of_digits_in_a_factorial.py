n = int (input("enter number"))
num = 1
for i in range (1,n+1):
    num = num * i
sum =0
temp = num
while temp > 0:
    sum = sum + temp % 10
    temp //= 10
print("sum of digits in factorial: ",sum)
    
