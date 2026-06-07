# Read N
n = int(input())
if(n>0):
  value = 1
  for i in range(n):
    print(value, end=" ")
    value=value*(n-1-i)//(i+1)
else:
  print(1)