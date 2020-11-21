# Function definitions for my functions

def my_abs(x):
    av = None
    if int(x) < 0:
        return 0 - int(x) 
    else:
        return int(x)

def my_gcd(num, den):
    gcd = None
    smaller = None
    larger = None

    if int(num) == 0:
        return int(den)

    # figure out which is larger 
    
    if my_abs(num) > my_abs(den):
        smaller = den
        larger = num
    else:
        smaller = num
        larger = den

    # calculate gcd

    for i in range(my_abs(smaller)):
        if smaller % (i + 1) == 0 and larger % (i + 1) == 0:
            gcd = i + 1 

    return gcd 
