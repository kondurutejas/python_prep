# Read total seconds
total = int(input())
h=total//3600
m=(total%3600)//60
s=total%60
print(f"{h}h {m}m {s}s")


