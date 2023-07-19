def pyt(a):
    s=0
    while a>0:
        s=s+(a%10)**2
        a=a//10
    return s

n=int(input())
r=n
while r>9:
    r=pyt(r)
if r==1 or r==7:
    print("True")
else:
    print("False")