from src.utils import custom_input

def proj_sieve_of_eratosthenes():
    print("Calculate primes up to...")
    num = custom_input("Limit 4,000,000", dtype='int')
    print(sieve_of_eratosthenes(num))

def sieve_of_eratosthenes(num):
    primes = [True for i in range(num + 1)]
    p = 2

    while (p * p <= num):
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(2, num + 1) if primes[i]]
