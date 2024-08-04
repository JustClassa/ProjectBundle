from src.utils import custom_input

# Project 9: Binary to Decimal and Back converter
def proj_bin_dec_converter():
    bin_or_dec = custom_input('1.) Binary to Decimal 2.) Decimal to Binary:', ['1', '2'])
    x = custom_input('Number to convert:', dtype='int')
    if bin_or_dec == "1":
        print(binary_to_decimal(x))
    elif bin_or_dec == "2":
        print(decimal_to_binary(x))

def binary_to_decimal(num: int) -> int | str:
    """
    A binary to decimal number converter.

    Args:
        num (int): The binary number to be converted.

    Returns:
        int: A decimal conversion of the binary number.
        str: An error message if the number is not binary.
    """
    for c in str('num'):
        if c not in ['0', '1']:
            return "Please input a binary number."

    decimal, i = 0, 0
    while (num != 0):
        dec = num % 10
        decimal += dec * pow(2, i)
        num //= 10
        i += 1
    return decimal

def decimal_to_binary(num: int) -> int:
    """
    A recursive decimal to binary number converter.

    Args:
        num (int): The decimal number to convert to binary.

    Returns:
        int: An integer representing a binary number.
    """
    if num == 0:
        return ''
    else:
        return f'{decimal_to_binary(num // 2)}{num % 2}'
