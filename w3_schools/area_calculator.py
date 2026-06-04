import math

# Read the shape
shape = input().strip()
if shape=="rectangle":
    a=int(input())
    b=int(input())
    c=a*b
elif shape=="triangle":
    a=int(input())
    b=int(input())
    c=a*b/2
elif shape=="circle":
    a=int(input())
    c=math.pi*a*a
print(f"Area: {c:.2f}")