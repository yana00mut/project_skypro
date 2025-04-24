import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("3296837868705121", "3296 83** **** 5121"),
        ("5273982176737348", "5273 98** **** 7348"),
        ("5537414228426789", "5537 41** **** 6789"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "number_acc, expected1",
    [
        ("73654108430135874305", "**4305"),
        ("73654430135874305", "**4305"),
        ("73654108430135879024305", "**4305")
    ],
)
def test_get_mask_account(number_acc: str, expected1: str) -> None:
    assert get_mask_account(number_acc) == expected1
