t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    minn=arr[0]
    for i in arr:
        if(minn>i):
            minn=i
    count=0
    for i in arr:
        if(i!=minn):
            count+=1
    print(count)
    
