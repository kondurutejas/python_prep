# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
total = 0
for i in range(n):
    total += numbers[i]
    print(total, end=" ")