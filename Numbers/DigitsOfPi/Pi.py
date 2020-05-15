import argparse
#use the decimal module to handle large precision values
from decimal import Decimal as Dec, getcontext as gc

if __name__=="__main__":
    skip=False
else:
    skip=True

##### If called from terminal: parse command line arguments #####
if not skip:
    parser = argparse.ArgumentParser(prog="Pi",description="This program displays the digits of Pi to a specified decimal place (up to 1000).",
        epilog="The value for Pi is determined by the Chudnovsky Approximation. Error from first 100 known digits of Pi is displayed as well.\n")
    parser.add_argument('digits', metavar='d', type=int, nargs='?',default=5,help="number of digits to be printed to the terminal. Defaults to 5.")
    parser.add_argument('-v',type=bool,nargs='?',default=False,help="Change to expanded output")
    
    args=parser.parse_args()

    N=args.digits

    if N > 1000:
        parser.error("[-d] Usage: Number of digits must be less than 1000.")


##### first 100 digits for comparison #####
pi = Dec('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

##### Chudnovsky Algorithm for Pi #####
##
## INPUT(s): < n : integer>
##           -Takes an integer value representing the desired number of decimal places to display Pi
## OUTPUT(s): < [ans,err] : list<Decimal> >
##            -Return a list object containing Pi and the error from first 100 digits known of Pi.
def Chudnovsky(n):
    gc().prec = n

    if n>1000:
        raise Exception(f"User entered [{n}]: out of bounds exception.\nValue must be <=1000.")
    
    #initialize
    _sum=0    
    C=Dec(426880)*Dec(10005).sqrt()
    M,L,X=Dec(1),Dec(13591409),Dec(1)
    _sum+=Dec(M*L)/Dec(X)

    #The number of iterations: the chudnovsky algorithm calculates ~14 decimal places per iteration
    #so to cut excess iterations we look at the number of desired decimal places
    k=n//14

    #produce next summation terms
    for i in range(0,k):
        L+=Dec(545140134)
        X*=Dec(-262537412640768000)
        M*=Dec((12*i+2)*(12*i+6)*(12*i+10)/((i+1)**3))
        _sum+=Dec(M*L)/Dec(X)
    ans=C/_sum

    #determine error
    err=Dec(ans-pi)

    return [ans,err]

##### If called from command terminal #####
if not skip:
    ans=Chudnovsky(N)
    if args.v:
        response=f"Pi: {ans[0]}\n\nErr: {ans[1]}"
    else:
        response=f"{ans[0]}"
    print(response)
