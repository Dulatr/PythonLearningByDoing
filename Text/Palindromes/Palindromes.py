"""
Collection of methods to determine if string is a palindrome.
"""
# Chain method for range objects
from itertools import chain

spec1 = range(32,47)
spec2 = range(58,64)
spec3 = range(91,96)
spec4 = range(123,126)
special_characters = chain(spec1,spec2,spec3,spec4)
special_characters = [chr(item) for item in special_characters]
special_characters.append('–')

#### METHODS ####
def isPalindrome(string):
    """
    Check string for palindrome using recursion. Returns boolean.

    Each recursive call reduces the size of string by 2.
    Making it run at O(n) complexity. 
    """
    if string == '':
        return True
    if string[0].lower() == string[-1].lower():
        string = rm(string,0)
        string = rm(string,-1)
        if isPalindrome(string):
            return True
    return False

def alternate(string):
    """
    Easy method for finding a palindrome using slicing.
    """
    if string == string[::-1]:
        return True
    return False
      
def rm(string,index):
    """
    Remove a character from a string at specified index
    """
    if index >= 0:
        return string[:index] + string[index+1:]
    return string[:index]

def rmSpecial(string):
    """
    From the list of special ascii characters, remove all if found in string.
    """
    for item in string:
        if item in special_characters:
            string = rm(string, string.index(item))
    return string
