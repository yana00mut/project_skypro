import pytest

from src.widget import get_date, get_mask_card_number


@pytest.mark.parametrize(
    "acc, expected",
    [
        ("Maestro 3296837868705121", "Maestro 3296 83** **** 5121"),
        ("Visa 5273982176737348", "Visa 5273 98** **** 7348"),
        ("Visa 5537414228426789", "Visa 5537 41** **** 6789"),
        ("Счет 98214164126421883067", "Счет **3067")
    ],
)
def test_mask_account_card(acc: str, expected: str) -> None:
    assert get_mask_card_number(acc) == expected


@pytest.mark.parametrize("acc", ["", None, "gdfngdf gdf", "1234", "867524565463"])
def test_mask_account_card_invalid(acc: str) -> None:
    """проверка на typeerror"""
    if acc is None:
        with pytest.raises(TypeError):
            get_mask_card_number(acc)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2023-08-15", "15.08.23"),
        ("2000-01-01", "01.01.00"),
        ("2024-03-11T02:26:18.671407", "11.03.24"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
