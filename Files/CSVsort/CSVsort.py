"""
A CSV record sorting CLI.
"""
import Parse as p
from FileIO import *
import Sort as s
from pathlib import Path

args = p.parse()

if not p.checkExt(args):
    raise Exception(f"File name {args.infile[0].name} missing csv extension.")
if args.o != None:
    if Path(Path.cwd().__str__() + '/' + args.o.name).is_file():
        response = input("Outfile name already exists, do you wish to continue? (y/n):> ")
        if response in ('n','N','no','No','NO'):
            args.o.close()
            exit()

# retrieve TextIOwrapper
infile = args.infile[0]

headers = getHeader(infile,row=args.row)

if not (args.label[0] in headers):
    raise ValueError(f"{args.label[0]} not in headers:{headers[:10]}...")

# reset stream position
infile.seek(0,0)

content = getContent(infile,row=args.row)
infile.close()

# check base case
if len(content) == 0:
    print("No data for fields. Returning...")
    exit()
elif len(content[0]) ==1:
    print("Only one data point per field. Returning...")
    exit()

if not args.row:
    content = s.transpose(content)
    content.sort(reverse=(not args.a),key=lambda data: data[headers.index(args.label[0])])
    content = s.transpose(content)
else:
    content.sort(reverse=(not args.a),key=lambda data: data[headers.index(args.label[0])])    

# recombine elements to string for writing
content = [','.join(item) for item in content]
if not args.row:
    content = [headers[i] + ',' + content[i] for i in range(0,len(headers))]
    content = '\n'.join(content)
else:
    headers = ','.join(headers) + '\n'
    content = headers + '\n'.join(content)

outfile = '.'
if args.o is None:
    outfile = outfile.join(('sorted_' + infile.name).split('.'))
    print(f'\nNo outfile name provided, saving file as: "{outfile}"...')
    if Path(Path.cwd().__str__() + '/' + outfile).is_file():
        response = input("File already exists. Overwrite? (y/n):> ")
        if response in ('n','N','no','No','NO'):
            exit()
    try:
        with open(outfile,'w') as file:
            file.write(content)
    except:
        print(f"Error opening file '{outfile}' for writing.")
else:
    args.o.write(content)
    args.o.close()