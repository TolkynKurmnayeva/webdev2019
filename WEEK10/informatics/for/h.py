n= int(input())
s=''
for i in range(1,n+1):
    if n%i==0:
        s+=str(i)+' '
print (s)
