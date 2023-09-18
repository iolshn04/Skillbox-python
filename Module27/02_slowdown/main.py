# TODO здесь писать код
import functools
import time
from typing import Callable, Any


def decorator(func: Callable) -> Callable:
    """
    Декоратор, замедляющий выполнение функции на заданное количество секунд.

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(3)
        result = func()
        return result

    return wrapper


@decorator
def check_data() -> Any:
    print('Проверяю изменения!')


check_data()

# зачтено
