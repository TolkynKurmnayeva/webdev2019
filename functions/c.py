def xor (a,b):
    return int(a!=b)
l=str.split(input())
a,b=float(l[0]),int(l[1])
print(xor(a,b))