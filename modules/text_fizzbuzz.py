from src.utils import custom_input
from typing import List

def proj_fizz_buzz():
    classic_toggle = custom_input("1.) Classic or 2.) Custom", [1, 2], dtype = "int")
    if classic_toggle == 1:
        print(fizz_buzz())
    elif classic_toggle == 2:
        input_quantity = custom_input("How many divisors and string would you like to use? (up to 10)", 
                                      [1, 2, 3, 4, 5, 6, 7 ,8 , 9, 10], 
                                      dtype='int')
        divisors = []
        strings = []
        for _ in range(input_quantity):
            divisors.append(custom_input ("What divisor would you like to use?", dtype='int'))
            strings.append(custom_input(f"What string would you like with {divisors[-1]}?"))

        array = custom_input("We should translate from 1 to --", dtype='int')
        print(fizz_buzz(divisors, strings, array))



def fizz_buzz(divisors: List[int] = [3, 5], strings: List[str] = ["Fizz", "Buzz"], array_length: int = 100) -> List:
    """
    FizzBuzz is a classic coding problem. This algorithm is an advanced fizz buzz creater

    Args:
        divisors (List[int]): List of divisors to translate to strings
        strings (List[str]): List of strings to translate divisors.
        array_length (int): Length of list to translate.

    Returns:
        List[str, int]: List of translated variables with the untranslated numbers.
    """
    if len(divisors) != len(strings):
        return "Divisors and strings need to be equal in number."
    
    dictionary_test = {n: string for n, string in zip(divisors, strings)}
    result = []

    for num in range(1, array_length + 1):
        construct = ''

        for div, string in dictionary_test.items():
            if num % div == 0:
                construct += string

        if construct == '':
            result.append(num)
        else:
            result.append(construct)

    return result

if __name__ == "__main__":
    fizz_buzz()