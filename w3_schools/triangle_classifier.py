# Read three sides
a = int(input())
b = int(input())
c = int(input())
if(a+b<=c or a+c<=b or b+c<=a):
    print("Not a triangle")
elif(a==b==c):
  	print("Equilateral")
elif(a==b	or b==c	or c==a):
  	print("Isosceles")
else:
  	print("Scalene")