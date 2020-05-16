# Reversing Strings

The problem is say we have some string available but we need to reverse the order instead of sorting. There are multiple ways to handle this: 

* Explicit loop
* List comprehension
* Recursion

and others I'm certain. The ways in which I've worked through the problem in this project is both a list comprehension and a recursive method. As for an explanation of the two I'll start with the list. A list comprehension is described in the form:

```python
    [(EXPRESSION) for (ITEM) in (LIST)]

    [(EXPRESSION) for (ITEM) in (LIST) if (CONDITION)]
```

In my example we create a list of characters using the comprehension:
```python
    [string[i] for i in range(len(string)-1,-1,-1)]
```
Which means for every character in the `string` at position `i`, start at position `len(string)-1` and work backwards while storing that character at the new position. Easy one line solution to the problem! Now for the recursion method there's a bit more going on. The idea behing recursion is that every new call of the method should reduce the difficulty of the problem. As in, we're taking a big problem and breaking it down into a series of tiny problems that we can handle much easier. So the method continues to call itself until the problem can't be broken down any further. Now the following section of code achieves the exact same thing as the list comprehension:
```python
    def recRev(string):

    # base case
    if len(string) < 2: 
        return string
    
    # remove a character, repeat, build upwards
    return recRev(removeChar(string,0)) + string[0]
```
All that `removeChar(string,index)` does is remove the character at the specified index and return. The first thing to notice is that the base case is handled by determining if the string has 1 character or less in it, since then there would be nothing left to reverse. Then the recursive call is made taking a string that is one character shorter that before, specifically removing the 1st character in the string. To visualize a bit of what's happening we can consider an easy example.

```bash
    string = 'abc'

    'abc'  ==> 1st call
               <is it less than 2?> No  --> continue
               <remove 1st character>
    
    'bc'   ==> 2nd call
               <is it less than 2?> No  --> continue
               <remove 1st character>
    
    'c'    ==> 3rd call
               <is it less than 2?> Yes --> return 'c'
    
    'cb'   ==> 'c' was returned, now add 'b'
    
    'cba'  ==> 'cb' was returned, now add 'a'

    return 'cba'
```
Here we can see that the number of calls is linear with the size of the string. So the time complexity of this algorithm is `O(n)` where the size of the string is `n`. 

#### Example

The example file contained in this folder generates random strings with 10 characters to then reverse using both methods outlined above. Just call this with your specified interpreter to see that the strings are in fact reversed!