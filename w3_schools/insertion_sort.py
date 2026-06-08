# Read input
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(1, n):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key
    print(*numbers)