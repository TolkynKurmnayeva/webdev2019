s=0
n=input()
a=str.split(input())
for i in range(len(a)):
    if int(a[i])>0:
        s+=1
print(s)        