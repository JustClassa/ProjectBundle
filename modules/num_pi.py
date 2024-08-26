from src.utils import custom_input
from decimal import Decimal, getcontext
from math import factorial

def proj_pi():
    digits = custom_input("How many digits of pi?", dtype='int')
    getcontext().prec = digits
    pi_estimate = chudnovsky(0, digits)
    print(pi_estimate)

def den(k):
    a = Decimal(factorial(6*k) * (545140134*k+13591409))
    b = Decimal(factorial(3*k)*(factorial(k)**3)*((-262537412640768000)**k))
    res = a / b
    if k > 0:
        return res + den(k - 1)
    else:
        return res

def num(root_precision):
    p = getcontext().prec
    getcontext().prec = root_precision
    d = Decimal(10005).sqrt()
    getcontext().prec = p
    return 426880 * d

def chudnovsky(k, root_precision):
    return num(root_precision)/den(k)

if __name__ == "__main__":
    proj_pi()