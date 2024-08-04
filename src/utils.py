from typing import List, Union, Optional, Any
import numpy as np
import math

def custom_input(prompts: Union[List[str], str], valid_responses: Optional[List[Any]] = None, dtype: str = 'str') -> Union[List[Any], Any]:
    """
    A robust custom input function that takes a prompt as a string, an optional list of valid responses,
    and a dtype to be returned as a string.

    Args:
        prompts (list | str): A list of strings prompt to ask user for an input
        valid_responses (list, optional): A list of acceptable responses from the user in the preferred datatype
        dtype (str, optional): A string representing the desired data type of the input.
    
    Returns:
        list | str| int | float: The user input converted to the specified data type. 
        Returns a list if multiple prompts are given, or a single value if only one prompt is given.

    Raises:
        TypeError: If the prompt's argument is not a list or a string.
        ValueError: If an invalid data type is specified

    Example:
        >>> custom_input("Enter your age", dtype='int')
        Enter your age : 25
        25

        >>> custom_input(["Enter your name", "Enter your age"], dtype='str')
        Enter your name : John
        Enter your age: 25
        ['John', '25']

        >>> custom_input("Enter a number between 1 and 5", valid_responses = [1, 2, 3, 4, 5], dtype='int')
        Enter a number between 1 and 5 : 3
        3
    """
    if isinstance(prompts, str):
        prompts = [prompts]
    if not isinstance(prompts, list):
        raise TypeError("Prompts must be a list or a string.")

    results = []
    dtypes = {'str': str, 'list': list, 'int': int, 'float': float}

    dtype_func = dtypes.get(dtype)
    if dtype_func is None:
        raise ValueError("Invalid dtype specified")

    for prompt in prompts:
        while True:
            user_input = input(f'{prompt} : ')
            try:
                result = dtype_func(user_input)
                if valid_responses is not None and result not in valid_responses:
                    print(f"Invalid input. Please enter one of the following: {valid_responses}")
                    continue
                results.append(result)
                break
            except ValueError as e:
                print(f"Invalid {dtype}: {e}")

    return results if len(prompts) > 1 else results[0]

def grocery_list(items: List[str]) -> str:
    """
    Create a human-readable string from a list of items.
    
    Args: items (List[str]): List of items
    
    Returns:
        str: Human-readable list string.
    """
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f'{items[0]} and {items[1]}'
    else:
        grocery_list = ''
        for item in items[:-1]:
            grocery_list += f'{item}, '
        grocery_list += f'and {items[-1]}'
        return grocery_list


def pluralize(word: str, quantity: int) -> str:
    """
    Return the plural form of a word based on the specified quantity.

    Args:
        word (str): Singular form of the word.
        quantity (int): Quantity of the item.

    Returns:
        str: Pluralized string.
    """
    SPECIAL_CASES = {
        'y':  ('y',  'ies'),
        's':  ('s',  'ses'),
        'sh': ('sh', 'shes'),
        'ch': ('ch', 'ches'),
        'x':  ('x',  'xes'),
        'z':  ('z',  'zes'),
        'o':  ('o',  'oes')
    }

    if quantity == 1:
        return word

    for ending, (singular_suffix, plural_suffix) in SPECIAL_CASES.items():
        if word.endswith(ending):
            return word[:-len(singular_suffix)] + plural_suffix
    
    return word + 's'
    
def random_list():
    """
    This function returns a list of random numbers of a size specified by the user.

    Returns:
        List[int]: A random list of numbers.
    """
    prompts = ["Low digit", "High digit", "Size of list"]
    low, high, size = custom_input(prompts, dtype='int')
    return np.random.randint(low, high + 1, size)

if __name__ == '__main__':
    print("Testing: custom_input")
    print(custom_input("Does this prompt work?", ["y", "n"]))

    print("Testing: random number generator")
    print(random_list())

    print("Testing: pluralize")
    print(pluralize(custom_input("Word to be plural"), 36))
    print(pluralize(custom_input("Word to be singular"), 1))
