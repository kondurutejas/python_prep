̃t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    total_cost=sum(arr)
    after_buying = x
    for j in arr:
        if(j<=y):
            after_buying += 0
        else:
            after_buying += j-y
    if(after_buying<total_cost):
        print("COUPON")
    else:
        print("NO COUPON")