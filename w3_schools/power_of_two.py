# Read the number
n = int(input())
found=0
for i in range(31):
  if(n==2**i):
    found=1
    break
if(found==1):
  print("Yes")
else:
  print("No")
    