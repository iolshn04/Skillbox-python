import functools
from collections.abc import Callable


def decorate(func: Callable) -> Callable:
    """Декаоратор который кэширует (сохраняет для дальнейшего использования)
    результаты вызова функции и, при повторном вызове с теми же аргументами,
    возвращает сохранённый результат.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print('Возращаем из кеша')
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res

    return wrapper


@decorate
def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован

# зачтено
