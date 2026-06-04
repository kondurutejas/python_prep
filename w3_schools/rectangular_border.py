# Read input
width = int(input())
height = int(input())
for i in range(height):
    if(i==0 or i==height-1):
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")