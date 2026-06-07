# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
maxx=numbers[0]
minn=numbers[0]
for i in numbers:
  if(i>maxx):
    maxx=i
  if(i<minn):
    minn=i
print(f"Min: {minn}")
print(f"Max: {maxx}")