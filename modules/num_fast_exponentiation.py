from src.utils import custom_input

#Project 21: Fast Exponentiation
def proj_fast_exponentiation():
    """
    Prompts the user to input a base and an exponent, then calculates the result using fast exponentiation.
    
    Fast exponentiation, also known as Exponentiation by Squaring, is a method that reduces the number of
    multiplications needed to calculate the power of a number. Instead of multiplying the base by itself 
    repeatedly (linear approach), it takes advantage of the properties of exponents:
    
    - If the exponent is even, we can express it as (base^(exponent/2))^2, reducing the problem size by half.
    - If the exponent is odd, we can reduce it by one to make it even, and then use the above principle.
    
    This algorithm has a time complexity of O(log e), where e is the exponent, making it significantly faster
    for large values compared to the naive approach.
    """
    base = custom_input("Enter the base: ")
    exponent = custom_input("Enter the exponent: ")
    print(fast_exponentiation(base, exponent))

def fast_exponentiation(base, exponent):

    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half = fast_exponentiation(base, exponent // 2)
        return half * half
    else:
        return base * fast_exponentiation(base, exponent - 1)
