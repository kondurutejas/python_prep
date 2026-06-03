
n = str(input("enter string: "))
vowels = 0
consonants = 0
for i in n:
    if i in {"a","e","i","o","u"}:
        print(i,"is a vowel")
        vowels += 1
    else:
        print(i,"is a consonant")
        consonants += 1
print("vowels: ",vowels)
print("consonants: ",consonants)