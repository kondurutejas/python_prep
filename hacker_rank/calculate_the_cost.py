t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sum=0
    for j in range(n):
        if(a[j] >= x):
            sum += b[j]
    print(sum)