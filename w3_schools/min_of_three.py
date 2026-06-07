def min_of_three(a, b, c):
  if(a<b and a<c):
    return a
  elif(a>b and b<c):
    return b
  elif(c<b and c<a):
    return c
  else:
    return a

a = int(input())
b = int(input())
c = int(input())
print("Min: " + str(min_of_three(a, b, c)))
