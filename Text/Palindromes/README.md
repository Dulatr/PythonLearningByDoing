# Palindromes

A palindrome is a word, phrase or sentence that when spelled backwards it is the same as forwards ([wikipedia article](https://en.wikipedia.org/wiki/Palindrome)). For example:

> 11/11/11

> Redivider

> A man, a plan, a canal – Panama

Number sequences can also be a palindrome. 

# Checking

The script in this folder contains two ways of finding a palindrome; a recursion method of O(n) complexity and a method with slicing. The slicing method is the easiest of the two, so below is the recursion explanation.

```python
def isPalindrome(string):
    # base case is an empty string if following calls are successful
    if string == '':
        return True

    if string[0].lower() == string[-1].lower():
        # remove the first and last characters of the string
        # recursive call with reduced string
        if isPalindrome(string):
            return True
    return False
```

The goal of recursion is to alway reduce the problem size each time to break up the work needed to be done. In this case, removing the first and last characters from the string if they are a match, else breaking the recursion when not matching and returning false.