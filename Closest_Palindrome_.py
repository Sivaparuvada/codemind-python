def pal(n):
    s=0
    while n>0:
        s=s*10+(n%10)
        n//=10
    return s
    
n=int(input())
for i in range(n+1,99999):
    if pal(i)==i:
        a=i
        break
for i in range(n-1,1,-1):
    if pal(i)==i:
        b=i
        break
if a-n>n-b:
    print(b)
elif a-n<n-b:
    print(a)
else:
    print(b,a)