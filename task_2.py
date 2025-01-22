import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    '''
    Function is generate the list of unique integer numbers

    Input:
    MIN_NUM - the minimum number for the list
    MAX_NUM - the maximum number for the list
    QUANTITY - the number of numbers of the list

    Output:
    * List with QUANTITY unique integers from MIN to MAX
    '''
    random_list = []

    try:
        min_num, max_num, quantity = int(float(min_num)), int(float(max_num)), int(float(quantity))
    except Exception as e:
        print(e)
        return random_list
    else:
        if 0 < min_num < max_num <= 1000 and 0 < quantity <= (max_num - min_num + 1):
            while len(random_list) < quantity:
                random_num = random.randint(min_num, max_num)
                if random_num in random_list:
                    continue
                else:
                    random_list.append(random_num)

        random_list.sort()
        return random_list

if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(10, 49, 2)
    print("Ваші лотерейні числа:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(-10, 10, 5)
    print("Ваші лотерейні числа:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(1000, 1200, 10)
    print("Ваші лотерейні числа:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(10, 4, 5)
    print("Ваші лотерейні числа:", lottery_numbers)            

    lottery_numbers = get_numbers_ticket(10, 20, 10)
    print("Ваші лотерейні числа:", lottery_numbers)            

    lottery_numbers = get_numbers_ticket(10, 20, 4)
    print("Ваші лотерейні числа:", lottery_numbers)   

    lottery_numbers = get_numbers_ticket(10, 11, 2)
    print("Ваші лотерейні числа:", lottery_numbers)
    
    lottery_numbers = get_numbers_ticket(10, "twenty", "2")
    print("Ваші лотерейні числа:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(10, 20, "10.1")
    print("Ваші лотерейні числа:", lottery_numbers)
