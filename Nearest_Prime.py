def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
 
n=int(input())
while n>0:
    a=int(input())
    lp=0
    up=0
    for i in range(a,1,-1):
        if prime(i)==1:
            lp=i
            break
    for i in range(a+1,99999):
        if prime(i)==1:
            up=i
            break
    if a-lp>up-a:
        print(up)
    elif a-lp<up-a:
        print(lp)
    else:
        print(lp)
    n-=1