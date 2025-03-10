from calendar import month
from datetime import datetime


def mask_account_card(number: str):
    if "Счет" in number:
        first = number[:4]
        last = number[-3:]
        return f"{first} **** **** *{last}"
    else:
        first_one = number[:2]
        second_two = number[4:6]
        last_three = number[-3:]
        return f"{first_one}** {second_two}** **** *{last_three}"


def get_date(date: str):
    day = date[9:10]
    month = date[6:7]
    year = date[:4]
    res = f"{day}.{month}.{year}"
    return res
