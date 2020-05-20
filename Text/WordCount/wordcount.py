def words(string):
    string = string.split(' ')
    return len(string)
def sentences(string):
    string = string.split('.')
    return len(string)
def vowels(string):
    vowel = ['a','e','i','o','u']
    count = 0
    for item in string:
        for k in vowel:
            if item == k:
                count+=1
    return count
