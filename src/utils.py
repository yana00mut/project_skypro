import json
import os
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/utils.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


def load_transactions(file_path):
    logger.info(f"Загрузка транзакций из файла: {file_path}")

    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден: {file_path}")
        return []

    if os.path.getsize(file_path) == 0:
        logger.warning(f"Файл пустой: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций.")
                return data
            else:
                logger.warning(f"Ожидался список, но получен другой тип данных.")
                return []
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при чтении JSON из {file_path}: {e}")
        return []
