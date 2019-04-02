s=''
n=int(input())
a=str.split(input())
for i in range(len(a)//2):
        x=a[i]
        a[i]=a[n-i-1]
        a[n-i-1]=x
for i in range(len(a)):
        s+=a[i]+' '
print (s)