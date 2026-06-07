def count_digits(n):
    # Return the number of digits in n
    count=0
    while n>0:
      n//=10
      count+=1
    return count
n = int(input())
print("Digits: " + str(count_digits(n)))
