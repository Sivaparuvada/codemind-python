def prime(a):
    if a==1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1
n=int(input())
for j in range(n,9999):
    if prime(j)==1:
        a=j
        break
        
for i in range(n-1,0,-1):
    if prime(i)==1:
        b=i
        break
if a-n>n-b:
    print(n-b)
else:
    print(a-n)