word = input().strip().lower()
maxx=0
res=""
for i in range(len(word)):
  count=0
  for j in range(len(word)):
    if(word[i]==word[j]):
      count+=1
  if(count>maxx):
    maxx=count
    res=word[i]
  elif(count==maxx and word[i]<res):
    res=word[i]
print(res)