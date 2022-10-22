
a,b,c=map(int,input().split())
s=(a+b+c)/2
k=((s*(s-a)*(s-b)*(s-c))**(1/2))
l="{:.2f}".format(k)
print(l)