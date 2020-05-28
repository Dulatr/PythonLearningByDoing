import opencage.geocoder as geo
import pickle
import os

import haversine
import data
import args

arg = args.parse()

if not os.path.exists("key.pickle"):
    print("No key found.")
    print("If you need an API key please visit https://opencagedata.com/api.")
    print("The following prompt will be asked only once, and key will be saved to 'key.pickle' in current directory.\n")
    API_key = { 
        "name": input("Enter a name to associate this key with:> "),
        "key" : input("To utilize geocode please enter your API key:> ") 
    }  
    with open('key.pickle','wb') as file:
        pickle.dump(API_key,file)

# unpickle existing key
with open('key.pickle','rb') as file:
    GeoKey = pickle.load(file)

print("Query may take a moment...please wait.\n")

try:
    coder = geo.OpenCageGeocode(GeoKey['key'])
    city1 = data.coords(coder.geocode(arg.c[0]))
    city2 = data.coords(coder.geocode(arg.c[1]))
except geo.InvalidInputError as invalid:
    print(invalid)
except geo.NotAuthorizedError as auth:
    print(auth)
except geo.UnknownError as unknown:
    print(unknown)

if city1 == [] or city2 == []:
    raise ValueError("Opencage server returned no results for query. Check spelling?")

if arg.u == ['km']:
    r = (6378 + 6357)/2.0
else:
    r = (3963+3950)/2.0

distance = haversine.distance([city2,city1],r)

print('='*34)
print('<'," "*2,'city'," "*3,':',' ( lat , long )  >')
print('-'*34)
print(f"< {arg.c[0]:12}: ({city1[0]:3.5},{city1[1]:3.5}) >\n< {arg.c[1]:12}: ({city2[0]:3.5},{city2[1]:3.5}) >")
print('='*34)

print(f"\n{distance:5.5} {arg.u[0]}")