from typing import Callable, Dict

def caching_fibonacci() -> Callable[[int], int]:
    """
    Повертає функцію для обчислення чисел Фібоначчі з кешуванням результатів.

    Повертає:
    - Функцію, яка приймає ціле число (n) і повертає число Фібоначчі.
    """
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Обчислює n-те число Фібоначчі, використовуючи кешування для прискорення обчислень.

        Аргументи:
        - n: Ціле число, яке вказує на індекс числа Фібоначчі, яке потрібно обчислити.

        Повертає:
        - n-те число Фібоначчі.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
