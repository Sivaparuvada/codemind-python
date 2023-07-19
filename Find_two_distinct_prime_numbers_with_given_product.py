def prime(a):
    if a==1:
        return 0
    for i in range(2,a):
        if a%i==0:
            return 0
            break
    return 1

n=int(input())
c=1
for i in range(1,n):
    for j in range(1,n):
        if i*j==n and prime(i)==1 and prime(j)==1:
            print(i,j)
            c=0
    if c==0:
        break
if c==1:
    print("-1")