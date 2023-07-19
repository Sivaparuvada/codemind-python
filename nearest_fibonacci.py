n=int(input())
a=0
b=1
c=1
while c<=n:
    c=a+b
    a=b
    b=c
if c-n>n-a:
    print(a)
elif c-n==n-a:
    print(a,c)
else:
    print(c)
    