n=int(input())
a=0
b=1
c=0
print(a,b,end=" ")
while n-2>0:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n-=1