from src.utils import custom_input


# Project 33: Reverse String
def proj_reverse_string():
    text = custom_input("Enter a string to reverse.")
    reversed_string = reverse_string(text)
    print(f'Reversed string: {reversed_string}')

def reverse_string(text: str) -> str:
    """
    Reverses a string.

    Args:
        text (str): The text to reverse.

    Returns:
        str: Reversed string.
    """
    return text[::-1]
