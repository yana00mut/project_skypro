import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод в USD"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод в RUB"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Оплата в USD"
        },
        {"id": 4, "description": "Без валюты"}
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_gen = filter_by_currency(sample_transactions, "USD")
    result = list(usd_gen)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_no_matches(sample_transactions):
    eur_gen = filter_by_currency(sample_transactions, "EUR")
    result = list(eur_gen)
    assert len(result) == 0


def test_transaction_descriptions_all(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    result = list(desc_gen)
    assert len(result) == 4
    assert result == ["Перевод в USD", "Перевод в RUB", "Оплата в USD", "Без валюты"]


@pytest.mark.parametrize("count, expected", [
    (1, ["Перевод в USD"]),
    (2, ["Перевод в USD", "Перевод в RUB"]),
    (3, ["Перевод в USD", "Перевод в RUB", "Оплата в USD"])])

def test_transaction_descriptions_partial(sample_transactions, count, expected):
    desc_gen = transaction_descriptions(sample_transactions)
    result = [next(desc_gen) for _ in range(count)]
    assert result == expected

@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"])])


def test_card_number_generator_range(start, end, expected):
    card_gen = card_number_generator(start, end)
    result = list(card_gen)
    assert result == expected

def test_card_number_generator_start_greater_than_end():
    card_gen = card_number_generator(5, 4)
    result = list(card_gen)
    assert len(result) == 0

def test_card_number_generator_single():
    card_gen = card_number_generator(5, 5)
    result = list(card_gen)
    assert result == ["0000 0000 0000 0005"]