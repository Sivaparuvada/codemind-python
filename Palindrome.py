def fun(n):
    s=0
    while n>0:
        s=s*10+n%10
        n//=10
    return s
    
n=int(input())
if n==fun(n):
    print(True)
else:
    print(False)