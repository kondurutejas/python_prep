n = int(input("enter the number: "))
sum = 0
temp = n
while temp > 0:
    sum += temp % 10
    temp //= 10
print("sum of digits in a number: ",sum)


    

