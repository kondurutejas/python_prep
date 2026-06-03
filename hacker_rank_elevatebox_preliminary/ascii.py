s=input()
found=""
for i in s:
    if (i.isupper()):
        found+=i.lower()
    else:
        found+=i.upper()
print(found)
        