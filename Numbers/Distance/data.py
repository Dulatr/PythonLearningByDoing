def coords(obj):
    """
    Return the lat and long of an opencage server response
    """
    return (obj[0]['geometry']['lat'],obj[0]['geometry']['lng'])