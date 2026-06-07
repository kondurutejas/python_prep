# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
found={}
for i in numbers:
  if i in found:
    found[i]+=1
  else:
    found[i]=1
count=0
for i in found:
  if(found[i]==1):
    count+=1
print(f"Unique: {count}")
    

