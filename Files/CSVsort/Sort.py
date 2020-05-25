"""
Helper methods for sorting list data.
"""
def transpose(data):
    # check for not staggered list
    if isStaggered(data):
        raise ValueError("Cannot transpose a staggered list.")

    temp = [[[''] for i in range(0,len(data))] for i in range(0,len(data[0]))]

    for k in range(0,len(data[0])):
        for i in range(0,len(data)):
            temp[k][i] = data[i][k]

    return temp

def isStaggered(data):
    test = len(data[0])
    for item in data:
        if len(item) != test:
            return True
    return False