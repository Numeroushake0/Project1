import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа, які відокремлені пробілами у вхідному тексті.
    """
    pattern = r' (?P<number>\d+\.\d+) '
    for match in re.finditer(pattern, f' {text} '):  # Додаємо пробіли на краях
        yield float(match.group('number'))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, підсумовуючи всі числа з генератора.
    """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")