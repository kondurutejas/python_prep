n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
target = int(input())
count=0
for i in numbers:
  if(i==target):
    count+=1
print(f"Count: {count}")
    
  
  
  
  