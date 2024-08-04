from src.utils import custom_input

# Project 13: Credit Card Validator
def proj_cc_validator():
    card_num = custom_input("Enter your credit card number:")
    if credit_card_validator(card_num):
        print(f'{card_num}: VALID')
    else:
        print(f'{card_num}: INVALID')

def credit_card_validator(card_number: str) -> bool:
    """
    Validate a credit card using the Luhn algorithm.

    Args:
        card_number (str): The credit card number to validate.

    Returns:
        bool: True if the credit card is valid, False otherwise.
    """
    card_number = [int(num) for num in card_number]

    processed_digits = [num if i % 2 == 0 
                        else num * 2 - 9 if num * 2 > 9 
                        else num * 2 for i, num in enumerate(card_number)]

    return sum(processed_digits) % 10 == 0
