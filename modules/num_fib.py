from src.utils import custom_input


# Project 3: Fibonacci Sequence Project
def proj_fibonacci():
    n = custom_input(['How many numbers would you like to generate'], dtype='int')
    mode = custom_input(['Select mode: 1.) Last number 2.) All numbers:'], valid_responses=['1', '2'])
    print(fibonacci(n, mode))

def fibonacci(n: int, mode: str = '1'):
    """
    This function uses the tabulation dynamic programming method to create the fibonacci sequence.

    Args:
        n (int): The number of fibonacci digits to compute.
        mode (str): '1' returns the final digit of the sequence and '2' returns the entire list

    Returns:
        List[int]: The fibonacci numbers in order.
    """
    table = [0, 1]
    for _ in range(n-2):
        table.append(table[-2] + table[-1])

    if mode == '1':
        return [table[-1]]
    elif mode == '2':
        return table
    