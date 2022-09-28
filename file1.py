from array import *
x=array('i',[])
r=int(input("enter range:"))
for i in range(r):
    n=int(input("enter values"))
    x.append(n)
print(x)
for i in x:
    if i%2==0:
        print("even number")
    else:
        print("odd number")
