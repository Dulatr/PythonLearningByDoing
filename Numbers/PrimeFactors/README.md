# Prime Factorization

This algorithm takes a number and breaks it down into it's base prime factors with no repeats and returns the list of primes. It's a simple command line script that takes a single integer argument.

bash
```bash
# return all prime factors of 15
./primes.py 15

$ [1, 3, 5, 15]
```

# Time Complexity

### Breakdown of code

```python
number = # some number

# base case is trivial
if number == 1:
    return number

# for every integer up to number (start at 2 since 1 is a given)
for n in range(2,number):
    # if integer evenly divides into the number
    if number % n == 0:
        # store as a prime

# for every evenly divisible value in number
for k in range(1,len(primes)):
    # look through previous values
    for m in range(1,k):
        # if current value in primes is divisible by any previous in list,
        if primes[k] % primes[m] == 0:
            # remove it
```
So the best case scenario is trivial, where 1 is simply returned making it `O(1)`. The first loop is straight forward and runs `n` times, with `n=number`, so this loop is `O(n)`. The final loop is trickier in that it varies dramatically with the number of primes found for `number`. The final loop consists of `k` iterations with `m` sub-iterations. Therefore, it runs `k*m` times or `O(k*m)`. Putting this we can determine an upper bound of `O(n^2)` since `m < k < n`. 

Bounds:
> O(n) < O(n + k*m) < O(n<sup>2</sup>)

Which we can typically say falls somewhere around:
> O(n * log n)

for the time complexity, even though the bounds aren't tight it's the best we can do in this scenario.
