__author__ = 'Adriana Jergusova'

def sort(a):
    """Sort the list `a` using selection sort."""
    n=len(a)
    for i in range(n):
        index=i
        for j in range(i + 1, n):
            if a[j] < a[index]:
                index = j
        a[i], a[index] = a[index], a[i]


# def worst_case(a):
#     n=len(a)
#     l2=len(a)
#     for i in range(len(a)):
#         l2[i]=a[n]
#         n-=1
#     return l2

# def repeat_elements(a):
#     pass

# def random(a):
#     pass

# def strings(a):
#     pass

