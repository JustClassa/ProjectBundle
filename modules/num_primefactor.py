from src.utils import custom_input
from typing import List


# Project 4: Prime Factorization
def proj_prime_factor():
    n = custom_input("Pick a number to factor.", dtype='int')
    print(f'The prime factors of {n} are: {prime_factor(n)}')

def prime_factor(n: int) -> List[int]:
    """
    This function factors a number (n) into its prime components.

    Args:
        n (int): The number to prime factor

    Returns:
        List[int]: The prime factors of n
    """
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    return factors
