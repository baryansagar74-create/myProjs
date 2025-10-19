n=int(input())
f= n*(n+1)//2
c=0
for i in range(0,n-1):
    a=int(input())
    c+=a
print(f-c)  
