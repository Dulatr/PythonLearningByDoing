################################################################
####        An example usage for the <reverse.py> file      ####
################################################################
import random 
import reverse as r

# Generate some random string to reverse
# using only capital letters for readability
random.seed()
string=''
for i in range(0,10):
    rands=random.randrange(65,90)
    string+=chr(rands)       

print("------------------------------------")
print("    Using the recursive function    ")
print("------------------------------------\n")
print(f"starting string : {string}\n")
print(f"ending string   : {r.recRev(string)}\n")

string=''
for i in range(0,10):
    rands=random.randrange(65,90)
    string+=chr(rands)

print("------------------------------------")
print("      Using list comprehension      ")
print("------------------------------------\n")
print(f"starting string : {string}\n")
print(f"ending string   : {r.reverse(string)}\n")