n = int(input())
temp=n
summ=0
while temp>0:
  digit=temp%10
  summ+=digit
  temp//=10
print(summ)