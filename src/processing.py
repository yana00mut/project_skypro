from calendar import month


def filter_by_state(spisok):
    state = "EXECUTED"
    new_spisok = []
    for i in spisok:
        if i.get("state") == state:
            new_spisok.append(i)
    return new_spisok


def sort_by_date(spisok):
    for i in spisok:
        data = i["date"]
        year = i[:4]
        monthh = i[5:7]
        num = i[9:11]

    new_spisok = sorted(spisok, reverse = True)

=======
from datetime import datetime


def filter_by_state(data, state="EXECUTED"):
    """Фильтрует список словарей по значению ключа state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data, descending=True):
    """Сортирует список словарей по значению ключа date"""
    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending
    )
