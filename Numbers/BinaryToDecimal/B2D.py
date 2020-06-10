# Binary numbers are prefixed with 0b
val = 0b101101

# When printed, the value is converted to it's decimal representation
print(val)

new_val = 50

# bin() converts a decimal to it's binary representation
print(f"50 in binary: {bin(new_val)}")

def two_complement(binary: int):
    # check for 8 or 16 bit
    temp = binary

    # invert
    temp = ~temp
    # add 1
    temp += 1
    
    return temp
print(two_complement(7))