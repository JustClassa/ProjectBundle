from src.utils import custom_input

# Project 17: Happy Numbers
def proj_happy_numbers():
    num = custom_input("Pick a number. Any number.", dtype='int')
    print(happy_numbers(num))

def happy_numbers(num: int) -> str:
    """
    Determine if a number is a happy number.

    Args:
        num (int): The number to check.

    Returns:
        str: a message indicating whether the number is happy or not.
    """
    def sum_of_squares(n):
        return sum(int(c) ** 2 for c in str(n))

    seen = set()

    while num!= 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)

    if num == 1:
        return f"{num} is a happy number."
    else:
        return f"{num} is NOT a happy number!"
