from random import randrange

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''
    Function is generate the list of unique integer numbers

    Input:
    MIN - the minimum number for the list
    MAX - the maximum number for the list
    QUANTITY - the number of numbers of the list
    
    Output:
    * List with QUANTITY unique integers from MIN to MAX
    '''
    pass

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)