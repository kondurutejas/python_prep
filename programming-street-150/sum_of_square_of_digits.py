n = int(input("enter a number : "))
sum =0 
temp = n
while temp>0:
    digit = temp % 10
    sum += digit ** 2
    temp //= 10
print("sum of squares of digits in a number: ",sum)