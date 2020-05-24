"""
A CSV record sorting CLI.
"""
import lib.Parse as p
from lib.FileIO import *
import lib.Sort as s

args = p.parse()

if not p.checkExt(args):
    raise Exception(f"File name {args.infile[0].name} missing csv extension.")

# retrieve TextIOwrapper
infile = args.infile[0]

# store headers
headers = getHeader(infile,row=args.row)
print(headers)
# reset stream position
infile.seek(0,0)

# store data
content = getContent(infile,row=args.row)

print(content)
print(s.sort(content,1))