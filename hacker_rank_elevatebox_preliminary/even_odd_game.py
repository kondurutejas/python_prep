n=int(input())
temp=n
sum_= 0
while temp>0:
    digit = temp%10
    sum_ += digit
    temp = temp//10
if(sum_ %2==0):
    print("Vignesh")
else:
    print("Charan")
