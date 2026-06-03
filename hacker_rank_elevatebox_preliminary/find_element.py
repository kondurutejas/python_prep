n=int(input())
arr=list(map(int,input().split()))
x=int(input())
found=0
for i in range(n):
    if(x==arr[i]):
        found=1
        break
    else:
        found=0
if(found==1):
    print(i)
else:
    print("-1")
        