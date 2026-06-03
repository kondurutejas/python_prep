n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    for j in arr[::-1]:
        print(j,end=" ")
    print()
        