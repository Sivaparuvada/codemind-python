n=int(input())
while n>0:
    a=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(1,a):
        if l[i-1]>l[i]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(l)-min(l))
    n-=1