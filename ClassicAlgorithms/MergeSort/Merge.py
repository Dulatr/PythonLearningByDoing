"""
This module contains the merge and sort methods for the classic algorithm.
"""

def merge(a,b):
    """
    Merge portion of algorithm. Takes two list objects and checks the first element of each,
    ascending sort checks first element of each to determine which is less then adds them
    to the end of an empty list.
    """
    if not isinstance(a,list):
        raise TypeError(f"Error, iterable must be {type(list())}")
    if not isinstance(b,list):
        raise TypeError(f"Error, iterable must be {type(list())}")    
    
    c = []
    i = 0
    # semi sort
    while a != [] or b != []:
        if a == [] or b == []:
            break
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    # One list will be empty, add the
    # remaining elements
    while a != []:
        c.append(a[0])
        a.remove(a[0])
    while b != []:
        c.append(b[0])
        b.remove(b[0])
    
    return c

def Sort(data):
    """
    The merge sort algorithm. Split data recursively, sort and merge.
    """
    if not isinstance(data,(list,tuple)):
        raise TypeError(f"Error, iterable must be type {type(list())} or {type(tuple())}")
    if None in data:
        raise IndexError(f"Can't sort type {type(None)} in list or tuple")
    for item in data:
        if isinstance(item,str):
            raise IndexError(f"Can't sort type {type(str)} in list or tuple")

    if len(data) == 1:
        return data
    
    a = [0]*(len(data)//2)    

    # even and odd cases handle size
    if len(data) % 2 != 0:
        b = [0]*(len(a) + 1)
    else:
        b = [0]*(len(a))

    # split the data 
    for i in range(0,len(data)):
        if i <= len(a)-1:
            a[i] = data[i]
        else:
            b[i-len(a)] = data[i]

    a = Sort(a)
    b = Sort(b)

    return merge(a,b)
