from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number):
    """Определяем является ли счетом"""
    card_numbers = ''
    card_name = ''
    for i in card_number:
        if i.isdigit():
            card_numbers += i
        else:
            card_name += i
    if "Счет" in card_number:
        result = get_mask_account(card_numbers)
    else:
        result = get_mask_card_number(card_numbers)
    return f"{card_name} {result}"


def get_date(date: str):
    """выводим дату"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    res = f"{day}.{month}.{year}"
    return res
