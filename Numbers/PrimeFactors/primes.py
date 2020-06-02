#!/usr/bin/python3.8
import argparse as ap

parser = ap.ArgumentParser(description="prime factorization")
parser.add_argument("value",action="store",type=int,help="number to factorize")
args = parser.parse_args()

def prime(val):
    primes = [1]
    
    if val == 1:
        return primes

    for n in range(2,val):
        if val % n == 0:
            primes.append(n)
    
    temp = primes[:]

    for k in range(1,len(primes)):
        if primes[k] > 3:
            for m in range(1,k):
                if primes[k] % primes[m] == 0:
                    temp.remove(primes[k])
                    break
        
    temp.append(val)

    return temp

print(prime(args.value))