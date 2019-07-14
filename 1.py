maa=int(input())
qaa=[]
for i in range(0,maa):
  raa=input()
  qaa.append(raa)
saa=[]
for i in zip(*qaa):
  if(i.count(i[0])==len(i)):
    saa.append(i[0])
  else:
    break
print(''.join(saa))
