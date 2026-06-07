# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
target = int(input())
found=0
for i in range(n):
  for j in range(i+1,n):
    if(numbers[i]+numbers[j]==target):
      print(numbers[i],numbers[j])
      found=1
      break
  if(found==1):
      break
if(found==0):
  print("No pair found")