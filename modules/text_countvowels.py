from src.utils import custom_input

def proj_count_vowels():
    text = custom_input("Give a string to count its vowels.")
    vowel_count = count_vowels(text)
    print(vowel_count)

def count_vowels(text: str) -> int:
    """
    Counts the vowels in a given string.

    Args:
        text (str): The string to count vowels for.

    Returns:
        int: The number of vowels.
    """
    result = 0
   
    for c in 'aeiou':
        result += text.count(c)

    return result