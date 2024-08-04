from typing import Dict
from src.utils import custom_input, pluralize, grocery_list


CURRENCY_DENOMINATIONS = {
    'one hundred dollar bill': 10000,
    'fifty dollar bill':       5000,
    'twenty dollar bill':      2000,
    'ten dollar bill':         1000,
    'five dollar bill':        500,
    'one dollar bill':         100,
    'quarter':                 25,
    'dime':                    10,
    'nickel':                  5,
    'penny':                   1
}

# Project 8: Change Return Program
def proj_change_return():
    cost, payment = custom_input(['What is the cost?', 'What is the payment?'], dtype='float')
    cost, payment = round(cost, 2), round(payment, 2)
    change = change_return(cost, payment)

    if "error" in change:
        print(change["error"])
        return
    
    change_breakdown = [f'{count} {pluralize(denomination, count)}' for denomination, count in change.items()]
    change_breakdown = grocery_list(change_breakdown)
    print(f'Change to be returned: {change_breakdown}')

def change_return(cost: float, payment: float) -> Dict[str, int]:
    """
    Calculate the change to be returned.

    Args:
        cost (float): The total cost.
        payment (float): The total payment.

    Returns:
        Dict[str, str]: A string providing an error statement.
        Dict[str, int]: The change breakdown in different denominations.
    """
    if payment < cost:
        return{"error": "Payment amount is less than the purchase price"}
    
    change = round((payment - cost) * 100)

    change_breakdown = {}
    for key, value in CURRENCY_DENOMINATIONS.items():
        count = change // value
        if count > 0:
            change_breakdown[key] = count
            change -= value * count
    
    return change_breakdown