from typing import Callable, Generator
import re


def generator_numbers(text: str) -> Generator[float, None, None]:
    for match in re.finditer(r'\b\d+\.\d+\b', text):
        yield float(match.group())
        

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> int:
    """
    Функція повертає суму всіх чисел, які знаходить та повертає нам генератор
    """
    return sum([n for n in func(text)])


text = "Загальний дохід працівника складається з декількох частин: \
    1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
