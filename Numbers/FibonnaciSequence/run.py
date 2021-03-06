from fib import fib
import argparse as ap

# Parse Arguments
parser=ap.ArgumentParser(description="Fibonnaci sequence generator")
parser.add_argument("-l",type=int,nargs='?',default=10,help="Length of the sequence to be shown. Default 10.")
args=parser.parse_args()

# Ensure argument actually passed
if args.l == None:
    parser.error("[-l] must be followed by an integer value.")

# Warn the user if they try to output large sequence list
# and prompt them to continue
if args.l >= 10000:
    warn = input("\nWARNING! : Very large sequence lengths take a long time to print as well as memory issues. Future versions may improve on this.\n"
        +"\nDo you wish to continue? y/n: ")
    if warn == 'n' or warn == 'N':
        exit()
    else:
        print('continuing..')
        fib(args.l)
else:
    print(fib(args.l))