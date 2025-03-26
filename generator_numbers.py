import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує числа з плаваючою комою, знайдені в заданому тексті.

    Аргументи:
    - text: Рядок, в якому будуть шукатися числа з плаваючою комою.

    Повертає:
    - Генератор, який повертає числа з плаваючою комою, знайдені в тексті.
    """
    pattern = r'\b\d+\.\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює суму чисел, згенерованих функцією з тексту.

    Аргументи:
    - text: Рядок, з якого будуть згенеровані числа.
    - func: Функція, яка приймає рядок і повертає генератор чисел з плаваючою комою.

    Повертає:
    - Сума чисел, згенерованих функцією.
    """
    return sum(func(text))
