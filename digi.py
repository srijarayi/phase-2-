n=1234
c=0
c1=0
while n>0:
    rem=n%10
    if rem%2==0:
        c+=1
    else:
        c1+=1
        
    n=n//10
print(c)
print(c1)
