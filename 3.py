infile=open("infile.txt",'r')
s=infile.read()
infile.close()
s=s.splitlines()
c=0
for i in s:
   a=input(i[:-1])
   if a==i[-1]:
       c+=1
       print("true")

name=input("enter your name")
print("go to result file")
print(name+"   ",c)
outfile=open("a.txt","w")
outfile.write(name+"   "+str(c))
outfile.close()