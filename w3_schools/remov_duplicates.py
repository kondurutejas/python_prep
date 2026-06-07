# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
a=[]
for i in numbers:
  if i not in a:
    a.append(i)
print(*a)