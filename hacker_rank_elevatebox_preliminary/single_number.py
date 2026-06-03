n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if (arr.count(i)==1):
        print(i)
        break