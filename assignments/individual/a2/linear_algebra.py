"""A linear algebra module.

This is a collection of functions dealing with vectors and matrices.
"""

__author__ = 'Adriana Jergusova'

import math

def vmagnitude(v : list[float]) -> float:
    """Returns the magnitude of the vector v (which may be of any
    length).

    This is found by adding up the squares of all of the elements of v
    and taking the square root of the total.
    """
    mag=0
    x=0
    while x<len(v):
        mag=mag+pow(v[x],2)
        x+=1
    mag=math.sqrt(mag)
    return mag

def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w.

    This is a vector of the same length, each of whose elements is the
    sum of the corresponding elements in v and w.
    """
    sum=[]
    x=0
    while x<len(v) and x<len(w):
       sum.append(v[x]+w[x])
       x+=1
    return sum

def vdifference(v : list[float], w : list[float]) -> list[float]:
    """Returns the difference between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    difference between the corresponding elements in v and w.
    """
    dif=[]
    x=0
    while x<len(v) and x<len(w):
       dif.append(v[x]-w[x])
       x+=1
    return dif

def velementwise_product(v : list[float], w : list[float]) -> list[float]:
    """Returns the element-wise between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    product of the corresponding elements in v and w.
    """
    "multiplying sections of arrays together"

    prod=[]
    x=0
    while x<len(v) and x<len(w):
       prod.append(w[x]*v[x])
       x+=1
    return prod

def vdot_product(v : list[float], w : list[float]) -> float:
    """Returns the dot product of vectors v and w.

    This is the sum of the products of the corresponding elements.
    """
    "adding multiplications together"
    sum_prod=0
    x=0
    while x<len(v) and x<len(w):
        sum_prod=sum_prod+(v[x]*w[x])
        x+=1
    return sum_prod

def mdimensions(m : list[list[float]]) -> list[int]:
    """Returns, as an array of two elements, the dimensions of matrix m."""
    "figure out number of rows and colnums"
    rows=len(m)
    x=0
    col=len(m[0])

    return [rows,col]

def msum(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise sum of matrices m and n."""
    sum = []
    for i in range(len(m)):
        r = []
        for j in range(len(m[i])):
            r += [None]
        sum += [r]
    y=0
    for x in range(len(m)):
        while y<len(m[x]):
            sum[x][y]=m[x][y]+n[x][y]
            y+=1
        y=0
    return sum

def melementwise_product(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise product of matrices m and n."""
    prod = []
    for i in range(len(m)):
        r = []
        for j in range(len(m[i])):
            r += [None]
        prod += [r]

    for x in range(len(m)):
        for y in range(len(m[x])):
            prod[x][y]=m[x][y]*n[x][y]
    return prod

def mtranspose(m : list[list[float]]) -> list[list[float]]:
    """Returns the transpose of m, that is, a matrix where element i, j
    is element j, i from m.
    """
    pose = []
    height =len(m)
    width = len(m[0])

    for i in range(width):
        r = []
        for j in range(len(m)):
            r += [0]
        pose += [r]

    for x in range(len(m)):
        for y in range(len(m[x])):
            pose[y][x]=m[x][y]
    return pose

def mproduct(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the matrix product of m and n.

    (Search the web for a definition.)
    """
    prod = []
    for i in range(len(m)):
        r = [0]*len(n[i])
        prod += [r]

    
    #prod = []
    #r = [0]*len(n[i])
    #for i in range(len(m)):
    #    prod.append(r)

    common=len(m[0])

    for x in range(len(prod)):
        for y in range(len(prod[x])):
            for index in range(common):
                prod[x][y]+=m[x][index]*n[index][y]
    return prod
