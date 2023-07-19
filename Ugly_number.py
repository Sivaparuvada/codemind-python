n=int(input())
while n%2==0 or n%3==0 or n%5==0:
    if n%2==0:
        n//=2
    elif n%3==0:
        n//=3
    elif n%5==0:
        n//=5
if n==1:
    print("Ugly Number")
else:
    print("Not Ugly Number")