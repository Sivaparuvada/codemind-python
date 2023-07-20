n=int(input())
l=list(map(int,str(n)))
s=0
for i in range(len(l)):
    s=s+l[i]**(i+1)
if s==n:
    print("True")
else:
    print("False")