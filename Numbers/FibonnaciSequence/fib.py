#### Fibonnaci sequence ####
#
# INPUT(s): [n] : [int]
#           -Length of desired sequence output.
#
# OUPUT(s): [...] : [List]
#           -Outputs a list of integers representing the sequence.
def fib(n):
    if n==0:
        return []
    elif n<=2:
        sequence=[0,1]
        return sequence[:n]
    elif n > 2:    
        sequence=[0]*n    
        sequence[1]=1

        for i in range(2,n):
            sequence[i]=sequence[i-1]+sequence[i-2]

        return sequence


    