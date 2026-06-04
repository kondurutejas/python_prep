# Read the sentence
sentence = input().strip()
# Find and print the longest word
w=sentence.split()
long=w[0]
for i in w:
  	if(len(i)> len(long)):
				long=i
print(long)