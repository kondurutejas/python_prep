n = int(input("enter start range: "))
m = int(input("enter end range: "))
sum = 0
for i in range(n,m+1):
    if i%2==0:
        sum = sum+i
print("sum of even numbers in the range: ",sum)
