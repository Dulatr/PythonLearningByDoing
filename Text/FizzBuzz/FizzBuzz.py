# Generate list of numbers
fb = [i for i in range(1,101)]

# Start loop
for i in range(0,len(fb)):
    # The trickiest part is realizing that you have to check both conditions first
    # unless you determine what numbers are divisible by 5 and 3 (ie. 15)
    if fb[i] % 3 == 0 and fb[i] % 5 == 0:
        fb[i] = "FizzBuzz"
    elif fb[i] % 5 == 0:
        fb[i] = "Buzz"
    elif fb[i] % 3 == 0:
        fb[i] = "Fizz"
print(fb)