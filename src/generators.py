def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по заданной валюте и возвращает итератор."""
    for transaction in transactions:
        if ("operationAmount" in transaction
                and "currency" in transaction["operationAmount"]
                and transaction["operationAmount"]["currency"].get("code") == currency_code):
            yield transaction


def transaction_descriptions(transactions):
    """Функция берет список транзакций и отдает описание каждой по очереди"""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start, end):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        num_str = str(number)
        while len(num_str) < 16:
            num_str = "0" + num_str
        card = f"{num_str[0:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield card
