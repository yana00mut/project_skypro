
from calendar import month
from datetime import datetime


def get_mask_card_number(number: str):
    """Срезаем числа"""
    first = number[:13]
    second = number[14:18]
    third = number[18:20]
    last = number[-4:]
    """Срезаем числа"""
    return f"{first} {second} {third}** **** {last}"


def get_mask_account(number: str):
    """Возвращаем замаскированное число"""
    once = number[-4:]
    return f"**{once}"


def get_date(date: str):
    """"Выводим дату"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    res = f"{day}.{month}.{year}"
    return res
