s=''
n=input()
a=str.split(input())
for i in range(len(a)):
    if int(a[i])%2==0:
        s+=a[i]+' '
print(s)        