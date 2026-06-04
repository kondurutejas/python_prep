# Read the string
text = input().strip()
v = ""
for i in text:
    if i not in v:
        v += i
print(v)