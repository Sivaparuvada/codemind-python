n=int(input())
c=1
if n==1:
    print("not a prime")
for i in range(2,n):
    if n%i==0:
        print("not a prime")
        c=0
        break
if c==1:
    print("prime")