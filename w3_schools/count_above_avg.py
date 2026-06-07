# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
summ=0
count=0
for i in numbers:
  summ+=i
  avg=summ/n
for i in numbers:
  if(i>avg):
    count+=1
print(f"Above average: {count}")