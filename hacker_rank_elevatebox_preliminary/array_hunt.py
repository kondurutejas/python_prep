n,x=map(int,input().split())
a=list(map(int,input().split()))
found=0
for i in range(n):
    if(a[i]==x):
        found = 1
        break
if(found==1):
    print("YES")
if(found!=1):
    print("NO")
    
        