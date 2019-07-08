def avgr(lst_ab):
    return sum(lst_ab)//len(lst_ab)
inp = int(input())
lst = [int(x) for x in input().split()]
lst1 = []
for i in range(len(lst)-1):
    if avgr(lst[0:i+1]) == avgr(lst[i+1:inp]):
        lst1.append('yes')
    else:
        lst1.append('no')
if 'yes' in lst1:
    print('yes')
else:
    print('no')
