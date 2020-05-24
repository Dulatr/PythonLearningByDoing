def sort(data,_key=0):
    temp = [item.split(',') for item in data]
    temp.sort(key=lambda col: col[_key])
    return temp