def get_mask_card_number(number: str):
    first = number[:4]
    second = number[4:6]
    last = number[-4:]
    return f"{first} {second}** **** {last}"


def get_mask_account(number: str):
    once = number[-4:]
    return f"**{once}"
