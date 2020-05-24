"""
The argument parsing methods for the CSVsort program.
"""
import argparse as ap
from lib.document import Doc

def parse():
    """
    Parse commandline arguments, load Doc information for desriptions.

    Returns <argparse.Namespace>
    """
    parser = ap.ArgumentParser(prog=Doc.name,description=Doc.description)

    # positional args  
    parser.add_argument('label',type=str,nargs=1,help=Doc.label)
    parser.add_argument('row',default='',nargs=1,help=Doc.row)
    parser.add_argument('infile',nargs=1,type=ap.FileType('r'),help=Doc.infile) 
    
    # optional args
    parser.add_argument('--version',action='version',version=f"{Doc.name} {Doc.version}",help=Doc.v_description)
    parser.add_argument('-a',nargs=1,default=['T'],help=Doc.ascending)
    parser.add_argument('-d',nargs=1,default=['F'],help=Doc.descending)
    parser.add_argument('-o',type=ap.FileType('w'),nargs='?',help=Doc.outfile)
    
    args = parser.parse_args()

    # convert string arguments to boolean
    args.row = str2Bool(args.row[0])
    args.a = str2Bool(args.a[0])
    args.d = str2Bool(args.d[0])

    return args

def checkExt(args,key='infile'):
    """
    Check argparse.Namespace for filename extension matching CSV
    from the argument key.

    Returns boolean.
    """
    if not isinstance(args,ap.Namespace):
        raise TypeError(f"Passed {type(args)}: Expected {ap.Namespace}")
    
    condition = False
    for _key,item in args._get_kwargs():
        if _key == key:
            fileinfo = item[0].name.split('.')
            filetype = fileinfo[len(fileinfo)-1].lower()
            if filetype == 'csv':
                return True
    return False

def str2Bool(string):
    """
    A helper method that converts a string to a boolean.
    """
    truth = ['True','false','T','t']
    false = ['False','false','F','f','']
    if string in truth:
        return True
    elif string in false:
        return False
    else:
        raise ap.ArgumentTypeError(f"{string} not a boolean value. Expected: {truth + false}")