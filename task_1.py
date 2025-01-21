import re
from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    '''
    Function returns cont of days from today to DATE_STR

    Input:
    * DATE_STR - date as the string

    Output:
    * Count of the date to the DATE_STR (integer)
    '''

    date_str_norm = re.sub(r'[\-\/\.:]', '-', date_str)

    try:
        days_left = (datetime.strptime(date_str_norm, '%Y-%m-%d') - datetime.now()).days
    except ValueError:
        print(f"'{date_str}' - does not match format 'YYYY-MM-DD'")
        return None
    except Exception as e:
        print(e)
        return None
    else:
        return days_left

if __name__ == "__main__":
    print(get_days_from_today("2025-02-24"))
    print(get_days_from_today("2022.02.24"))
    print(get_days_from_today("1926/01/01"))
