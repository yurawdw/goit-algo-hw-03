from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    '''
    Function returns cont of days from today to DATE_STR

    Input:
    * DATE_STR - date as the string

    Output:
    * Count of the date to the DATE_STR (integer)
    '''
    days_left = (datetime.strptime(date_str, '%Y-%m-%d') - datetime.now()).days
    return days_left

if __name__ == "__main__":
    print(get_days_from_today("2025-02-24"))
    print(get_days_from_today("2022-02-24"))

