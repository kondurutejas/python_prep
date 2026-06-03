n=int(input())
a=[]
for i in range(n):
    arr=list(map(int,input().split()))
    a.append(arr)
for i in range(n):
    r=0
    c=0
    for j in range(n):
        r+=a[i][j]
        c+=a[j][i]
    print(r+c,end=" ")