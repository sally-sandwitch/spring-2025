def fac(n:int) -> int:
    if n==1: return 1
    return n* fac(n-1)

print (fac(1))
print (fac(2))
print (fac(3))
print (fac(4))
print (fac(5))
print (fac(6))