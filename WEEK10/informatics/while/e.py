s=False
n=input()
a=str.split(input())
for i in range(1,len(a)):
    if int(a[i])//int(a[i-1])>0:
        s+=True
if s : 
        print('YES')
else: 
        print('NO')        