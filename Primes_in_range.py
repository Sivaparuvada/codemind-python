def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
    
a=int(input())
b=int(input())
c=0
while a<=b:
    if prime(a):
        c+=1
    a+=1
print(c)