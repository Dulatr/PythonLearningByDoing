"""
This module provides interaction with a FileIOwrapper to retrieve data from a CSV file.

All methods expect '\n' and ',' characters seperating date.
"""

def getHeader(IOwrapper,row=False):
    """
    Returns the header for rows or columns of a csv as a list of strings.
    """
    try:

        content=IOwrapper.read().split('\n')
        num_rows = len(content)
       
        if num_rows < 1:
            raise Exception()
        if num_rows == 1:
            return content[0].split(',')

        if row:
            temp = [item.split('\n') for item in content]
            temp = [item[0].split(',')[0] for item in temp]
            return temp
        else:
            temp = [item.split('\n') for item in content]
            return temp[0][0].split(',')
    
    except Exception:
        print("File too short for retrieving header. Empty file?")

def getContent(IOwrapper,row=False):
    """
    Returns the content body for rows or columns of csv as a list of strings.
    """
    try:
        content = IOwrapper.read().split('\n')
        num_rows = len(content)

        if num_rows < 1:
            raise Exception()
        if num_rows == 1:
            return ''     
        if row:
            pass
        else:
            content.remove(content[0])
        
        return content

    except Exception:
        print("File too short for retrieving content. Empty file?")
