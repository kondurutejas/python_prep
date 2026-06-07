def is_palindrome(word):
  pal=word[::-1]
  if(pal==word):
    return True
  else:
    return False
word=input()
if(is_palindrome(word)):
  print("Yes")
else:
  print("No")

