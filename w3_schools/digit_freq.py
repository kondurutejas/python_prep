# Read the number as a string
num = input().strip()
for digit in "0123456789":
  count=0
  for i in num:
    if(i==digit):
      count+=1
  if(count>0):
    print(f"{digit}:{count}")