from array import *
a=array('i',[])
n=int(input("enter n:"))
for i in range(n):
    x=int(input("enter value:"))
    a.append(x)
print(a)
ele=int(input("enter search no:"))
k=0
for i in a:
    if i==ele:
        print(k)
    k=k+1
else:
    print("not found")
