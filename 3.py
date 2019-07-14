strr11,strr22=input().split()
length=len(strr11) if len(strr11)<len(strr22) else len(strr22)
diff=abs(len(strr11)-len(strr22))
counts=diff
for i in range(length):
  if(len(strr22)==1 and strr22[i] in strr11):
    break
  if(strr11[i]!=strr22[i]):
    counts+=1
print(counts)
