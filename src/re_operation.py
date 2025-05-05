import re


def filter_by_description(operations: list[dict], search_string: str) -> list[dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get("description", ""))]


def count_by_category(operations: list[dict], categories: list[str]) -> dict:
    result = {category: 0 for category in categories}
    for op in operations:
        desc = op.get("description", "").lower()
        for category in categories:
            if category.lower() in desc:
                result[category] += 1
    return result
