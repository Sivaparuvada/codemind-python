def rev(n):
    s=0
    while n>0:
        s=s*10+n%10
        n//=10
    return s
    
n=int(input())
while n:
    n+=rev(n)
    if rev(n)==n:
        print(n)
        break