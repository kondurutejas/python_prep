# Read the number
n = int(input())
count=0
for i in range(100000):
  if(n==1):
    break
  if(n%2==0):
    n=n//2
  else:
    n=n*3+1
  count+=1
print(f"Steps: {count}")
  
