
from src.masks import get_mask_card_number, get_mask_account, number

if "Счет" in number:
    result = get_mask_account() # реализован в masks
else:
    result = get_mask_card_number()  # реализован в masks

