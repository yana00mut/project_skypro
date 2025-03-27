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

