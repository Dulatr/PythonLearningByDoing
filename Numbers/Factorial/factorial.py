# recursive factorial function
def factorialR(n):
    if not isinstance(n,int):
        raise Exception(f"Cannot take factorial of type {type(n)}")    
    if n < 0:
        raise Exception("Negative factorial undefined")

    if n == 0:
        return 1
    return n * factorialR(n-1)

# basic factorial approach
def factorial(n):
    if not isinstance(n,int):
        raise Exception(f"Cannot take factorial of type {type(n)}")    
    if n < 0:
        raise Exception("Negative factorial undefined")

    ans = 1
    while True:
        if n == 0:
            ans *= 1
            break
        else:
            ans *= n
            n -= 1
    return ans
