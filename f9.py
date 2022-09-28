from array import *
ar=array('i',[])
a=int(input("enter value:"))
for i in range(a):
    n=int(input("values=:"))
    ar.append(n)
for i in ar:
    print(i)
newar=array(ar,'i',(i*i for i in ar))
 #  newar.append(i)
for i in newar:
    print("new array=",i)
