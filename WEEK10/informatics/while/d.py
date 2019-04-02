s=0
n=input()
a=str.split(input())
for i in range(1,len(a)):
    if int(a[i])>int(a[i-1]):
        s+=1
print(s)        