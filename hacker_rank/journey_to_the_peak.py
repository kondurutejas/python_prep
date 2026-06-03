n=int(input())
arr=list(map(int,input().split()))
altitude=0
max_al=0
for i in arr:
    altitude += i
    if(altitude>max_al):
        max_al=altitude
print(max_al)
