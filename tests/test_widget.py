from src.masks import get_mask_card_number, get_mask_account, get_date
def test_standard_20_digit_number():
    """Тест для стандартного 20-значного номера"""
    input_number = "12345678901234567890"
    expected = "1234567890123 4567 89** **** 7890"
    assert get_mask_card_number(input_number) == expected