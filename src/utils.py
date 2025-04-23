import json
import os
import logging


if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

def load_transactions(file_path):
    logger.info(f"Загрузка транзакций из файла: {file_path}")
    if not os.path.exists(file_path):
        logger.error(f"Файл с транзакциями не найден: {file_path}")
        return []

    if os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Транзакции загружены успешно. Количество: {len(data)}")
                return data
            else:
                logger.warning("Неверный формат данных в файле транзакций")
                return []

    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []

file_path = "operations.json"


print(load_transactions(file_path))