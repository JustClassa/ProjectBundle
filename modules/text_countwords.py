from src.utils import custom_input

def proj_count_words():
    text = custom_input("Insert a string to count its words.")
    word_count = count_words(text)
    print(word_count)
    
def count_words(text: str) -> int:
    """
    Counts the number of words in a string.

    Args:
        text (str): A string to count the words for.

    Returns:
        int: The number of words.
    """
    return len(text.split(' '))
