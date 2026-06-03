t= int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if(x>y):
        a=(x-y)*z
        print(a)
    elif(x==y):
        print("0")
    else:
        print("Arjun has enough chocolates")