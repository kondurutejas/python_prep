t=int(input())
w,x,y,z=map(int,input().split())
if(x<(w+(y*z))):
    print("overflow")
elif(x==w+(y*z)):
    print("filled")
else:
    print("unfilled")