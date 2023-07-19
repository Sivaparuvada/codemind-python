def dig(n):
    c=0
    while n>0:
        c+=1
        n//=10
    return c


n=int(input())
m=n*n

l=pow(10,dig(n))
if n==m%l:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")