def fib(n:int)->int:
    return go(n,0,1)
def go(n:int,a:int, b:int)->int:
    if n==0:return a
    return go(n-1,b,a+b)

print(fib(950))