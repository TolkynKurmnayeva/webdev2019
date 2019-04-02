a,b,c,d= int(input()),int(input()),int(input()),int(input())
s=''
for i in range(a,b+1):
    if i%d==c:
        s+=str(i)+' '
print(s)        
