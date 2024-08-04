from src.utils import custom_input


# Project 34: Pig Latin
def proj_pig_latin():
    text = custom_input("Enter a string to translate to pig latin.")
    translated_text = pig_latin(text)
    print(translated_text)

def pig_latin(text: str) -> str:
    """
    Translates a string into pig latin

    Args:
        text (str): The string to translate

    Returns:
        str: The translation.
    """
    bag_of_words = [''.join(c.lower() for c in word if c.isalnum()) for word in text.split()]

    for i, word in enumerate(bag_of_words):
        if word[0] in 'aeiou':
            bag_of_words[i] = word + 'way'
        elif word[1] in 'aeiou':
            bag_of_words[i] = word[1:] + word[0] + 'ay'
        else:
            bag_of_words[i] = word[2:] + word[:2] + 'ay'
    
    return ' '.join(bag_of_words)
