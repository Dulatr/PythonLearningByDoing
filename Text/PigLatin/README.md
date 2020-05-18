# Pig Latin

Pig latin is a fun use of English jargon where you take the initial letter in a word, and add it to the end with the suffix 'ay'. There are a few simple rules when applying it that you can check out on the [wiki page](https://en.wikipedia.org/wiki/Pig_Latin#Rules). 

## Example 

In the [example.py](example.py) file, we take a string of text and get rid of any unwanted characters in the string before latinizing the words. 

```python
import latin

string = """ Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules"""

# ---------------------------------------------------------
# get the string in a format without any special characters
# ---------------------------------------------------------

# convert the string into a list of words
string = string.split()
# latinize each word
string = [latin.latinize(string[i]) for i in range(0,len(string)-1)]
# join the list back into a string
string = " ".join(string)
```

The above example then outputs the following string:
```python
"igPay atinLay isay aay amegay ofay alterationsay ayedplay onay ethay ishEnglay anguagelay amegay oTay eatecray ethay igPay atinLay ormfay ofay anay ishEnglay ordway ethay initialay onsonantcay oundsay isay ansposedtray otay ethay enday ofay ethay ordway anday anay ayay isay affixeday Exay ananabay ouldway ieldyay anana-bayay eadRay ikipediaWay orfay oremay informationay onay"
```
With a bit of extra work on the part of the user they can return the special characters removed. A good edition to this project would to be to attempt this.
