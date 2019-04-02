import math
a,b= int(input()),int(input())
s=''
for i in range(a,b+1):
    if math.sqrt(i)==math.floor(math.sqrt(i)):
        s+=str(i)+' '
print(s)        
