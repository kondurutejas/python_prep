# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
    count=0
    maxx=numbers[0]
for i in range(1,n-1):
  if(numbers[i]==numbers[i+1]):
    count+=1
    if(count>maxx):
      maxx=count
print(f"Longest streak: {maxx}")
    
    