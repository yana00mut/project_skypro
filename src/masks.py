import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/utils.log',
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

logger = logging.getLogger(__name__)


def get_mask_card_number(number: str):
    """Срезаем числа"""
    logger.info(f"Вызвана get_mask_card_number с аргументом: {number}")
    first = number[:13]
    second = number[14:18]
    third = number[18:20]
    last = number[-4:]
    result = f"{first} {second} {third}** **** {last}"
    logger.info(f"Результат: {result}")
    return result


def get_mask_account(number: str):
    """Возвращаем замаскированное число"""
    logger.info(f"Вызвана get_mask_account с аргументом: {number}")
    result = f"**{number[-4:]}"
    logger.info(f"Результат: {result}")
    return result


def get_date(date: str):
    """Выводим дату"""
    logger.info(f"Вызвана get_date с аргументом: {date}")
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    result = f"{day}.{month}.{year}"
    logger.info(f"Результат: {result}")
    return result

