from task_1 import get_days_from_today
from task_2 import get_numbers_ticket
from task_3 import normalize_phone

if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))

    print('*' * 50)
    print('')

    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    print('*' * 50)
    print('')

    raw_numbers = [
                    "067\\t123 4567",
                    "(095) 234-5678\\n",
                    "+380 44 123 4567",
                    "380501234567",
                    "    +38(050)123-32-34",
                    "     0503451234",
                    "(050)8889900",
                    "38050-111-22-22",
                    "38050 111 22 11   ",
                    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)    
    
    print('*' * 50)
    print('')
