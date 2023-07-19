def rev(n):
    s=0
    while n>0:
        s=s*10+n%10
        n//=10
    return s
    
n=int(input())
a=n*n
r=rev(a)
k=int(r**0.5)
if n==rev(k):
    print(True)
else:
    print(False)