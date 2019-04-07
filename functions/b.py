def power (a,n):
    if a==0:
        return a
    r=1
    for i in range(n):
        r*=a
    return r
l=str.split(input())
a,n=float(l[0]),int(l[1])
print(power(a,n))