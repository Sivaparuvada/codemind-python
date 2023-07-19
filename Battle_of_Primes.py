def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if n%i==0:
            return 0
    return 1
    
a=int(input())
b=int(input())
c=a+b
for i in range(c+1,10000):
    if prime(i)==1:
        print(i-c)
        break