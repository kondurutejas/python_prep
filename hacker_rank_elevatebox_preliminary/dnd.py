n,m=map(int,input().split())
arr=list(map(int,input().split()))
count=0
flag=0
for i in arr:
    if(i%m==0):
        count+=i
    else:
        flag+=i
a=count-flag
print(a)
        