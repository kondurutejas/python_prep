n = int(input("enter starting number: "))
m = int(input("enter ending number: "))
for num in range(n,m+1):
    sum = 0
    temp = num
    while temp>0:
        digits = temp %10
        sum = sum + digits **3
        temp //= 10
    if sum == num:
        print(f"{num} is an armstrong number")
   