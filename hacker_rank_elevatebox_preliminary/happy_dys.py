t=int(input())
for i in range(t):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    count=0
    for j in range(n):
        if(arr1[j]<= 2*arr2[j] and arr2[j]<= 2*arr1[j]):
            count = count+1
    print(count)
    