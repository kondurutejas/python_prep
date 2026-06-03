t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maxx = arr[0]
    for i in range(n):
        if(arr[i]>maxx):
            maxx = arr[i]
    print(maxx)
       
