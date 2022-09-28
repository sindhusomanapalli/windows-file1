n=int(input("enter no:"))
k=0
i=1
while n>=i:
    if n%i==0:
        print("number=",i)
        k=k+1
    i=i+1
print("count=",k)
