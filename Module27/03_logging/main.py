import datetime
import functools
from typing import Callable


def logging(func: Callable) -> Callable:
    """Декоратор, который отвечает за логирование функий"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function: {}".format(func.__name__))
        print("Documentation: {}".format(func.__doc__))

        try:
            return func(*args, **kwargs)
        except Exception as error:
            with open("function_errors.log", "a") as file:
                now = datetime.datetime.now()
                file.write(f"Function: {func.__name__}\n")
                file.write(f"Error: {str(error)}\n")
                file.write(f"DateTime: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("\n")

    return wrapper


@logging
def divide(a: int, b: int) -> int:
    """Функция делит первый аргумент на второй"""
    return a / b


@logging
def multiply(a: int, b: int) -> int:
    """Функция умножает два аргумента"""
    return a * b


print(divide("a", 5))
print(multiply(2, 5))

# зачтено
