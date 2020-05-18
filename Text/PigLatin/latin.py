# Vowel list
vowels=['a','e','i','o','u']

#####   Check for consonant
##
##  Takes a character input and compares it to the list of vowels
##
##  INPUTS: [character] : <chr>
##          -Character to check
##
##  OUTPUTS: <bool>
##           -Returns true or false
def isConsonant(character):
    for item in vowels:
        if character == item:
            return False
    return True

#####   Check for consonant cluster
##
##  Takes a string input to determine if leading characters are a consonant cluster
##
##  INPUTS: [string] : <str>
##          -String to check
##
##  OUTPUTS: <tuple>
##           -Returns a tuple containing a boolean and integer. If the string contains
##            a leading consonant cluster then the tuple contains (true,<index>) where
##            the integer is the index indicating the end of the cluster
def isCluster(string):
    n=0
    for char in string:
        if not isConsonant(char):
            break 
        n+=1   
    if n > 1:
        return (True, n)
    else:
        return (False, 0)

#####   Turn to Pig Latin
##
##  Takes a string input and returns a pig latin version
##
##  INPUTS: [string] : <str>
##          -string to convert
##
##  OUTPUTS: <str>
##           -Returns the pig latin version of the input string based on
##            rules.
def latinize(string):
    suffix = 'ay'

    if isConsonant(string[0]):
        test=isCluster(string)
        if(test[0]):
            string = string[test[1]:] + string[:test[1]] + suffix
            return string
        elif string[0] == 'h':
            return string + suffix
        else:
            string=string[1:] + string[0] + suffix
            return string
    else:
        return string + suffix

