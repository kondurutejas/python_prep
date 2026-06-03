n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    left=sum(arr[:i])
    right=sum(arr[i+1:])
    a=(abs(left - right))
    print(a,end = " ")