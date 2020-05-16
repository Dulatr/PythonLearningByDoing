####    Basic string reversal using list comprehension
## INPUTS: [string] : <str>
##         -string to be reversed
## OUTPUT: <str>
##         -Joined list of reversed characters
def reverse(string):
    temp=[string[i] for i in range(len(string)-1,-1,-1)]
    return "".join(temp)

####    Basic string reversal using recursion
## INPUTS: [string] : <str>
##         -string to be reversed
## OUTPUT: <str>
##         -Recursively built reversed string
def recRev(string):
    if len(string) < 2: 
        return string
    return recRev(removeChar(string,0)) + string[0]

####    String character removal
## INPUTS: [string] : <str>
##         -String to remove character from
##
##         [index]  : <int>
##         -index of the character you want removed.
##          
## OUTPUT: <str>
##         -Concatenated spliced string
def removeChar(string,index):
    return string[:index] + string[index+1:]

