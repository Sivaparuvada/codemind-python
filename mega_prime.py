def prime(a):
    if a==1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
            break
    return 1
n=int(input())
if prime(n)==1:
    while n>0:
        r=n%10
        if r==3 or r==5 or r==7 :
            c=0
        else:
            c=1
            print("Not Mega Prime")
            break
        n=n//10
    if c==0:
        print("Mega Prime")
else:
    print("Not Mega Prime")