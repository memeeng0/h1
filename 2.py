de=int(input('enter decimal '))
bi=[]
while de>0:
    bi.append(de%2)
    de//=2
bi.reverse()
for i in bi:
    print(i,end='')

