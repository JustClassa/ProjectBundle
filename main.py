import modules as md
from src.utils import custom_input
from src.title import title_screen


FUNCTIONS = {
    '3':  [md.proj_fibonacci, 'Fibonacci Sequence'],
    '4':  [md.proj_prime_factor, 'Prime Factorization'],
    '8':  [md.proj_change_return, 'Change Return'],
    '9':  [md.proj_bin_dec_converter, 'Binary to Decimal and Back Converter'],
    '13': [md.proj_cc_validator, 'Credit Card Validator'],
    '17': [md.proj_happy_numbers, 'Happy Numbers'],
    '25': [md.proj_sieve_of_eratosthenes, 'Sieve of Eratosthenes'],
    '32': [md.proj_fizz_buzz, 'Fizz Buzz'],
    '33': [md.proj_reverse_string, 'Reverse String'],
    '34': [md.proj_pig_latin, 'Pig Latin'],
    '35': [md.proj_count_vowels, 'Count Vowels'],
    '36': [md.proj_palindrome_checker, 'Palindrome Checker'],
    '37': [md.proj_count_words, 'Count Words'],
    '46': [md.proj_port_scanner, 'Port Scanner'],
    'q':  ['', 'Quit']
}

def game_loop():
    game_on = True
    title_screen()
    
    while game_on:
        module = select_module()

        if module.lower() == 'q':
            break

        FUNCTIONS[module][0]()
        
        input("Press 'Enter' to continue...")
    print("Bye for now!")

def select_module():
    modules = [f'{key}.) {value[1]}' for key, value in FUNCTIONS.items()]
    
    print("Please select a module")
    return custom_input(' '.join(modules), valid_responses=list(FUNCTIONS.keys()))
    
if __name__ == '__main__':
    game_loop()
