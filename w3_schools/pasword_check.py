# Read the password
password = input().strip()
n=len(password)
if(n>=8):
  print("Valid")
else:
  print("Invalid")