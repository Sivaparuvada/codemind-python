n=int(input())
for i in range(2**n):
    x=bin(i)
    print(x[2:].zfill(n))