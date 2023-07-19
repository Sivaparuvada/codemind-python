n=int(input())
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
maxi=0
c=0
while rev>0:
    if rev%10==6 and c==0:
        maxi=maxi*10+9
        c=1
    else:
        maxi=maxi*10+rev%10
    rev//=10
print(maxi)