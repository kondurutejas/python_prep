# Read the number
n = int(input())
summ=0
for i in range(1,n):
  if(n%i==0):
    summ+=i
if(summ==n):
  print("Yes")
else:
  print("No")
