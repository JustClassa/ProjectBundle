from src.utils import custom_input


# Project 36: Palindrome Checker
def proj_palindrome_checker():
    text = custom_input("Enter a potential palindrome.")
    if palindrome_checker(text):
        print(f'{text} is a palindrome.')
    else:
        print(f'{text} is not a palindrome.')

def palindrome_checker(text: str) -> str:
    """
    Checks if the given text is a palindrome.

    Args:
        text (str): The text to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    cleaned_string = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned_string == cleaned_string[::-1]
