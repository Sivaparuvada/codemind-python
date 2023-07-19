n=int(input())
sum=0
for i in range(n):
    if i*(i+1)==n:
        sum=1
        break
if sum==1:
    print("YES")
else:
    print("NO")