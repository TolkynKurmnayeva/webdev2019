s=''
n=input()
a=str.split(input())
for i in range(len(a)):
    if i%2==0:
        s+=a[i]+' '
print(s)        