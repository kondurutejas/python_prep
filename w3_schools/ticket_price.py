# Read age from input
age = int(input())
if(age<12):
  print("Child")
  print("$5")
elif(12<=age<=64):
  print("Adult")
  print("$15")
else:
  print("Senior")
  print("$8")