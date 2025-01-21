import re

def normalize_phone(phone_number) -> str:
    '''
    The function is convert the string that containing a telephone number

    Input:
    * phone_number - same the string

    Output:
    * the string of the phone number or None 
    '''

    phone_number = re.sub(r'\D+', '', phone_number)

    if phone_number != '':
        if not phone_number.startswith('380'): 
            if phone_number.startswith('0'):
                phone_number = '38' + phone_number
            else:
                phone_number = '380' + phone_number
        return '+' + phone_number
    else:
        return None

if __name__ == "__main__":
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
                    "äfweweaefaefefs"
                    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)