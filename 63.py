op=input()
ll=[]
for i in op:
    if i not in ll:
        ll.append(i)
        #print(i)
    else:
        break
print(len(ll))
