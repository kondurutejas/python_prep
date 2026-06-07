def double_all(numbers):
  number=[]
  for i in numbers:
    number.append(i*2)
  return number
n=int(input())
numbers=[]
for i in range(n):
  numbers.append(int(input()))
dou=double_all(numbers)
print(*dou)
                 