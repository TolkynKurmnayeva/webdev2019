def min (a,b,c,d):
    if a<=b and a<=c and a<=d:
        return a
    elif b<=c and a<=d:
        return b
    elif c<=d:
        return c
    else: 
        return d
l=str.split(input())
a,b,c,d=int(l[0]),int(l[1]),int(l[2]),int(l[3])
print(min(a,b,c,d))